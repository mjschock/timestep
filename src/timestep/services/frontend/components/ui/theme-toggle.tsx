"use client"

import { useTheme } from "./theme-provider"
import { Button } from "./button"
import { Moon, Sun } from "lucide-react"
import { Tooltip, TooltipContent, TooltipTrigger } from "./tooltip"
import { Icon } from "./icon"

export function ThemeToggle() {
  const { theme, setTheme, isLoaded } = useTheme()

  // Only render the toggle on the client after the theme has been loaded
  if (!isLoaded) {
    return <div className="h-9 w-9"></div> // placeholder with same dimensions
  }

  return (
    <div className="flex items-center space-x-2">
      <Tooltip>
        <TooltipTrigger asChild>
          <Button
            variant="ghost"
            size="icon"
            className="h-9 w-9 rounded-full bg-transparent dark:bg-transparent hover:bg-secondary dark:hover:bg-secondary transition-colors border-none outline-none cursor-pointer"
            style={{
              border: 'none',
              outline: 'none',
              boxShadow: 'none'
            }}
            onClick={() => setTheme(theme === "light" ? "dark" : "light")}
          >
            {theme === "light" ? (
              <Icon icon={Sun} className="h-5 w-5 text-foreground" />
            ) : (
              <Icon icon={Moon} className="h-5 w-5 text-foreground" />
            )}
            <span className="sr-only">Toggle theme</span>
          </Button>
        </TooltipTrigger>
        <TooltipContent>
          <p>Toggle theme</p>
        </TooltipContent>
      </Tooltip>
    </div>
  )
} 