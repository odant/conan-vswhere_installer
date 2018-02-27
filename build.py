import os
from conan.packager import ConanMultiPackager


# Common settings
username = "odant" if "CONAN_USERNAME" not in os.environ else None

    
if __name__ == "__main__":
    builder = ConanMultiPackager(
        username=username,
        exclude_vcvars_precommand=True
    )
    builder.add()
    builder.run()

