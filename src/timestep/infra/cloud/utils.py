from libcloud.compute.base import KeyPair, NodeDriver


def get_or_create_key_pair(node_driver: NodeDriver, name: str, content: str) -> KeyPair:
    # TODO: what about we want to delete the key pair? delete_key_pair

    key_pair: KeyPair | None = node_driver.get_key_pair(name=name)

    if not key_pair:
        key_pair: KeyPair = node_driver.create_key_pair(name=name, public_key=content)

    return key_pair
