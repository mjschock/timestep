# class K3Sup(Block):
#     _block_type_slug: str = "k3sup"

#     # comment: Optional[str] = f"{os.environ.get('USER')}@{socket.gethostname()}"
#     # key_type: Optional[str] = "ed25519"
#     # new_passphrase: Optional[SecretStr] = "''"
#     # output_keyfile: Optional[str] = f"{DIST_PATH}/.ssh/id_{key_type}"
#     # public_key: Optional[str] = None
#     private_key: Optional[SecretStr] = None

#     def block_initialization(self):
#         if self.public_key is None or self.private_key is None:
#             # comment = f"{os.environ.get('USER')}@{socket.gethostname()}"
#             # key_type = "ed25519"
#             # output_keyfile = f"{DIST_PATH}/.ssh/id_{key_type}"

#             if not os.path.exists(output_keyfile):
#                 os.makedirs(os.path.dirname(output_keyfile), exist_ok=True)

#                 with ShellOperation(
#                     commands=[
#                         f"k3sup install --context {config.KUBE_CONTEXT} --ip {cloud_instance_construct.data_source.ipv4} --local-path {config.KUBE_CONFIG_PATH} --skip-install --ssh-key {config.SSH_PRIVATE_KEY_PATH} --user ubuntu"
#                     ],
#                 ) as shell_operation:
#                     shell_process = shell_operation.trigger()
#                     shell_process.wait_for_completion()

#             # self.public_key = pathlib.Path(f"{output_keyfile}.pub").read_text()
#             # self.private_key = SecretStr(pathlib.Path(output_keyfile).read_text())
