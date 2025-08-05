import difflib
import json
import re
import uuid
from dataclasses import dataclass
from typing import Any


@dataclass
class ToolMatchResult:
    tool: dict[str, Any]
    confidence_score: float
    cost_breakdown: dict[str, float]
    extracted_params: dict[str, Any]


def create_fallback_tool_call(
    response: str, tools: list[dict[str, Any]], logger=None
) -> list[dict[str, Any]]:
    """
    Create an intelligent fallback tool call using language-agnostic schema-aware cost function.
    Works with any language and any tool schema.
    """
    if logger:
        logger.warning(
            "⚠️ WARNING: streaming tool_choice='required' but no tool calls found. "
            "Creating language-agnostic fallback tool call using schema-aware cost function."
        )

    if not tools:
        raise ValueError("No tools available for fallback")

    # Find best tool match using language-agnostic cost function
    best_match = find_best_tool_language_agnostic(response, tools, logger)

    # Add metadata with sorted cost breakdown
    best_match.extracted_params["__fallback_reason"] = "language_agnostic_schema_cost"
    best_match.extracted_params["__confidence_score"] = best_match.confidence_score
    best_match.extracted_params["__cost_breakdown"] = dict(
        sorted(best_match.cost_breakdown.items())
    )

    tool_calls = [
        {
            "id": f"call_{uuid.uuid4().hex[:8]}",
            "type": "function",
            "function": {
                "name": best_match.tool["function"]["name"],
                "arguments": json.dumps(best_match.extracted_params, sort_keys=True),
            },
        }
    ]

    if logger:
        logger.info(
            f"✅ Selected tool: {best_match.tool['function']['name']} (confidence: {best_match.confidence_score:.3f})"
        )

    return tool_calls


def find_best_tool_language_agnostic(
    response: str, tools: list[dict[str, Any]], logger=None
) -> ToolMatchResult:
    """
    Find the best matching tool using completely language-agnostic methods.

    Uses only:
    - Character-level edit distance
    - String similarity metrics
    - Universal structural patterns (numbers, brackets, quotes)
    - Schema structure analysis
    - No language-specific assumptions
    """
    best_result = None
    best_total_cost = float("inf")

    for tool in tools:
        result = calculate_language_agnostic_cost(response, tool, logger)
        total_cost = sum(result.cost_breakdown.values())

        if total_cost < best_total_cost:
            best_total_cost = total_cost
            best_result = result

        if logger:
            logger.debug(f"🎯 Tool '{tool['function']['name']}' cost: {total_cost:.3f}")

    return best_result


def calculate_language_agnostic_cost(
    response: str, tool: dict[str, Any], logger=None
) -> ToolMatchResult:
    """
    Calculate language-agnostic schema-aware cost using only universal patterns.

    Cost components (all language-independent):
    - string_similarity: Pure character/substring similarity
    - structural_compatibility: Universal patterns (numbers, quotes, brackets)
    - schema_coverage: Parameter type compatibility
    - lexical_overlap: Raw character sequence matching
    """
    tool_name = tool["function"]["name"]
    tool_description = tool["function"].get("description", "")
    parameters = tool["function"].get("parameters", {}).get("properties", {})

    costs = {
        "string_similarity": 1.0,
        "structural_compatibility": 1.0,
        "schema_coverage": 1.0,
        "lexical_overlap": 1.0,
    }

    # 1. STRING SIMILARITY (pure edit distance, language-agnostic)
    all_tool_text = f"{tool_name} {tool_description}"
    for param_name, param_spec in parameters.items():
        param_desc = param_spec.get("description", "")
        all_tool_text += f" {param_name} {param_desc}"

    # Calculate various similarity metrics
    similarity_scores = []

    # Edit distance similarity
    edit_ratio = difflib.SequenceMatcher(
        None, response.lower(), all_tool_text.lower()
    ).ratio()
    similarity_scores.append(edit_ratio)

    # Substring containment (bidirectional)
    response_lower = response.lower()
    tool_text_lower = all_tool_text.lower()

    # How much of tool text appears in response
    tool_in_response = calculate_substring_coverage(tool_text_lower, response_lower)
    similarity_scores.append(tool_in_response)

    # How much of response appears in tool text
    response_in_tool = calculate_substring_coverage(response_lower, tool_text_lower)
    similarity_scores.append(response_in_tool)

    # Longest common subsequence ratio
    lcs_ratio = longest_common_subsequence_ratio(response_lower, tool_text_lower)
    similarity_scores.append(lcs_ratio)

    avg_similarity = sum(similarity_scores) / len(similarity_scores)
    costs["string_similarity"] = 1.0 - avg_similarity

    # 2. STRUCTURAL COMPATIBILITY (universal patterns)
    structural_score = calculate_structural_compatibility(response, parameters)
    costs["structural_compatibility"] = 1.0 - structural_score

    # 3. SCHEMA COVERAGE (parameter type matching)
    coverage_score = calculate_universal_schema_coverage(response, parameters)
    costs["schema_coverage"] = 1.0 - coverage_score

    # 4. LEXICAL OVERLAP (character n-gram similarity)
    lexical_score = calculate_ngram_overlap(response, all_tool_text)
    costs["lexical_overlap"] = 1.0 - lexical_score

    # Extract parameters using language-agnostic methods
    extracted_params = extract_parameters_language_agnostic(response, tool, logger)

    # Calculate confidence
    total_cost = sum(costs.values())
    confidence_score = max(0.0, 1.0 - (total_cost / 4.0))

    return ToolMatchResult(
        tool=tool,
        confidence_score=confidence_score,
        cost_breakdown=costs,
        extracted_params=extracted_params,
    )


def calculate_substring_coverage(text1: str, text2: str, min_length: int = 3) -> float:
    """
    Calculate what fraction of text1 appears as substrings in text2.
    Language-agnostic string matching.
    """
    if not text1 or not text2:
        return 0.0

    # Generate all substrings of text1 of minimum length
    substrings = set()
    for i in range(len(text1) - min_length + 1):
        for j in range(i + min_length, len(text1) + 1):
            substring = text1[i:j]
            if len(substring) >= min_length:
                substrings.add(substring)

    if not substrings:
        return 0.0

    # Count how many substrings appear in text2
    matched_length = 0
    total_length = sum(len(s) for s in substrings)

    for substring in substrings:
        if substring in text2:
            matched_length += len(substring)

    return matched_length / total_length if total_length > 0 else 0.0


def longest_common_subsequence_ratio(text1: str, text2: str) -> float:
    """
    Calculate longest common subsequence ratio (language-agnostic).
    """

    def lcs_length(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    if not text1 or not text2:
        return 0.0

    lcs_len = lcs_length(text1, text2)
    max_len = max(len(text1), len(text2))

    return lcs_len / max_len if max_len > 0 else 0.0


def calculate_structural_compatibility(
    response: str, parameters: dict[str, Any]
) -> float:
    """
    Calculate structural compatibility using universal patterns that work in any language.
    """
    if not parameters:
        return 1.0

    structural_patterns = {
        "string": [
            r'["\']([^"\']*)["\']',  # Quoted strings (universal)
            r"[\u00C0-\u017F\u0100-\u024F\w]+",  # Unicode word characters
        ],
        "integer": [
            r"\b\d+\b",  # Integers (universal)
            r"[0-9]+",  # Digits (universal)
        ],
        "number": [
            r"\b\d*[.,]\d+\b",  # Decimals with . or , (both common)
            r"\b\d+[.,]?\d*\b",  # Numbers with optional decimal
        ],
        "boolean": [
            r"\b[01]\b",  # Binary digits (universal)
            # Note: removed language-specific true/false/yes/no
        ],
        "array": [
            r"\[[^\]]*\]",  # Square brackets (universal)
            r"\{[^}]*\}",  # Curly brackets (universal)
            r"\([^)]*\)",  # Parentheses (universal)
            r"[^,]+(?:,[^,]+)+",  # Comma-separated (common separator)
        ],
        "object": [
            r"\{[^}]*\}",  # JSON-like objects (universal)
            r"\[[^\]]*\]",  # Bracket notation (universal)
        ],
    }

    compatible_params = 0
    total_params = len(parameters)

    for param_name, param_spec in parameters.items():
        param_type = param_spec.get("type", "string")
        patterns = structural_patterns.get(param_type, structural_patterns["string"])

        # Check if any pattern matches
        for pattern in patterns:
            if re.search(pattern, response, re.UNICODE):
                compatible_params += 1
                break

    return compatible_params / total_params if total_params > 0 else 0.0


def calculate_universal_schema_coverage(
    response: str, parameters: dict[str, Any]
) -> float:
    """
    Calculate schema coverage using only universal, language-agnostic methods.
    """
    if not parameters:
        return 1.0

    coverage_scores = []

    for param_name, param_spec in parameters.items():
        coverage = 0.0

        # 1. Check if parameter name appears anywhere in response (exact match)
        if param_name.lower() in response.lower():
            coverage += 0.4

        # 2. Check if parameter name parts appear (split on common separators)
        param_parts = re.split(r"[_\-\.]", param_name.lower())
        for part in param_parts:
            if len(part) > 2 and part in response.lower():
                coverage += 0.2

        # 3. Check if parameter description words appear (if description exists)
        param_desc = param_spec.get("description", "")
        if param_desc:
            # Use character-level similarity for description
            desc_lower = param_desc.lower()
            response_lower = response.lower()
            similarity = difflib.SequenceMatcher(
                None, desc_lower, response_lower
            ).ratio()
            coverage += similarity * 0.4

        coverage_scores.append(min(1.0, coverage))

    return sum(coverage_scores) / len(coverage_scores)


def calculate_ngram_overlap(text1: str, text2: str, n: int = 3) -> float:
    """
    Calculate character n-gram overlap (language-agnostic).
    """

    def get_ngrams(text: str, n: int) -> set[str]:
        text = text.lower()
        return {text[i : i + n] for i in range(len(text) - n + 1)}

    if not text1 or not text2:
        return 0.0

    ngrams1 = get_ngrams(text1, n)
    ngrams2 = get_ngrams(text2, n)

    if not ngrams1 or not ngrams2:
        return 0.0

    intersection = len(ngrams1 & ngrams2)
    union = len(ngrams1 | ngrams2)

    return intersection / union if union > 0 else 0.0


def extract_parameters_language_agnostic(
    response: str, tool: dict[str, Any], logger=None
) -> dict[str, Any]:
    """
    Extract parameters using only language-agnostic, universal patterns.
    """
    extracted_params = {}
    parameters = tool["function"].get("parameters", {}).get("properties", {})

    if not parameters:
        return extracted_params

    for param_name, param_spec in parameters.items():
        param_type = param_spec.get("type", "string")

        # Try universal extraction strategies
        extracted_value = None

        strategies = [
            lambda pn=param_name: extract_by_exact_name_match(response, pn),
            lambda pt=param_type: extract_by_universal_type_patterns(response, pt),
            lambda pn=param_name: extract_by_proximity_to_name(response, pn),
            lambda pn=param_name: extract_by_position_patterns(response, pn),
        ]

        for strategy in strategies:
            try:
                extracted_value = strategy()
                if extracted_value is not None:
                    break
            except Exception as e:
                if logger:
                    logger.debug(f"Strategy failed: {e}")
                continue

        # Universal type coercion
        coerced_value = coerce_universally(extracted_value, param_type)

        if coerced_value is not None:
            extracted_params[param_name] = coerced_value
        else:
            extracted_params[param_name] = get_universal_default(param_type)

    return extracted_params


def extract_by_exact_name_match(response: str, param_name: str) -> Any:
    """Extract by finding exact parameter name in response."""
    # Look for param_name followed by common separator characters and a value
    separators = r"[:\-=\s]+"
    value_pattern = r"([^\s,;|\n]+)"

    pattern = rf"{re.escape(param_name)}{separators}{value_pattern}"
    match = re.search(pattern, response, re.IGNORECASE | re.UNICODE)

    if match:
        return match.group(1).strip()

    return None


def extract_by_universal_type_patterns(response: str, param_type: str) -> Any:
    """Extract based on universal type patterns that work in any language."""
    universal_extractors = {
        "string": lambda: extract_universal_string(response),
        "integer": lambda: extract_universal_integer(response),
        "number": lambda: extract_universal_number(response),
        "boolean": lambda: extract_universal_boolean(response),
        "array": lambda: extract_universal_array(response),
    }

    extractor = universal_extractors.get(param_type)
    if extractor:
        return extractor()

    return None


def extract_by_proximity_to_name(response: str, param_name: str) -> Any:
    """Extract values that appear near the parameter name."""
    # Find parameter name in response
    param_index = response.lower().find(param_name.lower())
    if param_index == -1:
        return None

    # Look for values within a window around the parameter name
    window_size = 50
    start = max(0, param_index - window_size)
    end = min(len(response), param_index + len(param_name) + window_size)
    window = response[start:end]

    # Extract any quoted string, number, or word from the window
    patterns = [
        r'["\']([^"\']+)["\']',  # Quoted strings
        r"\b\d+(?:[.,]\d+)?\b",  # Numbers
        r"\b[^\s,;|]+\b",  # Any word
    ]

    for pattern in patterns:
        matches = re.findall(pattern, window)
        if matches:
            return matches[0] if isinstance(matches[0], str) else str(matches[0])

    return None


def extract_by_position_patterns(response: str, param_name: str) -> Any:
    """Extract based on positional patterns relative to parameter name."""
    words = response.split()
    param_words = param_name.lower().split("_")

    # Find words similar to parameter name parts
    for param_word in param_words:
        if len(param_word) > 2:
            for i, word in enumerate(words):
                # Check similarity using edit distance
                similarity = difflib.SequenceMatcher(
                    None, param_word, word.lower()
                ).ratio()
                if similarity > 0.7 and i + 1 < len(words):
                    next_word = words[i + 1].strip(",:;")
                    if next_word:
                        return next_word

    return None


# Universal extraction helpers (language-agnostic)
def extract_universal_string(response: str) -> str | None:
    """Extract any string using universal patterns."""
    # Try quoted strings first
    quote_patterns = [r'"([^"]*)"', r"'([^']*)'", r"`([^`]*)`"]
    for pattern in quote_patterns:
        match = re.search(pattern, response)
        if match and match.group(1):
            return match.group(1)

    # Fall back to any non-whitespace sequence
    match = re.search(r"\S+", response)
    return match.group(0) if match else None


def extract_universal_integer(response: str) -> int | None:
    """Extract any integer using universal number patterns."""
    match = re.search(r"\b\d+\b", response)
    if match:
        try:
            return int(match.group(0))
        except ValueError:
            pass
    return None


def extract_universal_number(response: str) -> float | None:
    """Extract any number using universal patterns."""
    # Try different decimal separators
    patterns = [r"\b\d+\.\d+\b", r"\b\d+,\d+\b", r"\b\d+\b"]
    for pattern in patterns:
        match = re.search(pattern, response)
        if match:
            try:
                # Normalize decimal separator to dot
                number_str = match.group(0).replace(",", ".")
                return float(number_str)
            except ValueError:
                continue
    return None


def extract_universal_boolean(response: str) -> bool | None:
    """Extract boolean using only universal patterns (no language-specific words)."""
    # Use only numeric patterns: 1/0, or presence of numbers
    if re.search(r"\b1\b", response):
        return True
    elif re.search(r"\b0\b", response):
        return False

    # Could add more universal boolean indicators here
    return None


def extract_universal_array(response: str) -> list[str] | None:
    """Extract array using universal structural patterns."""
    # Try various bracket patterns
    bracket_patterns = [
        r"\[([^\]]*)\]",  # Square brackets
        r"\{([^}]*)\}",  # Curly brackets
        r"\(([^)]*)\)",  # Parentheses
    ]

    for pattern in bracket_patterns:
        match = re.search(pattern, response)
        if match and match.group(1).strip():
            content = match.group(1)
            # Split on common separators
            items = [item.strip().strip("\"'") for item in re.split(r"[,;|]", content)]
            return [item for item in items if item]

    return None


def coerce_universally(value: Any, param_type: str) -> Any:
    """Universal type coercion without language assumptions."""
    if value is None:
        return None

    try:
        if param_type == "string":
            return str(value).strip()
        elif param_type == "integer":
            if isinstance(value, str):
                # Extract first sequence of digits
                match = re.search(r"\d+", value)
                return int(match.group(0)) if match else None
            return int(value)
        elif param_type == "number":
            if isinstance(value, str):
                # Handle both . and , as decimal separators
                normalized = re.sub(r"[^\d.,]", "", value)
                normalized = normalized.replace(",", ".")
                match = re.search(r"\d*\.?\d+", normalized)
                return float(match.group(0)) if match else None
            return float(value)
        elif param_type == "boolean":
            if isinstance(value, str):
                # Only use numeric indicators
                return "1" in value or value.strip() == "1"
            return bool(value)
        elif param_type == "array":
            if isinstance(value, str):
                # Split on common separators
                items = [item.strip() for item in re.split(r"[,;|]", value)]
                return [item for item in items if item]
            return list(value) if hasattr(value, "__iter__") else [value]
        else:
            return value
    except (ValueError, TypeError):
        return None


def get_universal_default(param_type: str) -> Any:
    """Get universal default value for any parameter type."""
    defaults = {
        "string": "",
        "integer": 0,
        "number": 0.0,
        "boolean": False,
        "array": [],
        "object": {},
    }
    return defaults.get(param_type, "")
