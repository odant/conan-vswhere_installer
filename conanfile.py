from conans import ConanFile, tools


class VswhereInstallerConan(ConanFile):
    name = "vswhere_installer"
    version = "2.3.2"
    license = "MIT license - https://raw.githubusercontent.com/Microsoft/vswhere/develop/LICENSE.txt"
    description = "Visual Studio Locator"
    url = "https://github.com/odant/conan-vswhere"
    settings = {
        "os_build": ["Windows"]
    }

    def build(self):
        license_url = "https://raw.githubusercontent.com/Microsoft/vswhere/develop/LICENSE.txt"
        self.output.info("Download %s " % license_url)
        tools.download(license_url, "LICENSE.txt")
        vswhere_url = "https://github.com/Microsoft/vswhere/releases/download/%s/vswhere.exe" % self.version
        self.output.info("Download %s " % vswhere_url)
        tools.download(vswhere_url, "vswhere.exe")
        checksum = "103f2784c4b2c8e70c7c1c03687abbf22bce052aae30639406e4e13ffa29ee04"
        if tools.sha256sum("vswhere.exe") != checksum:
            raise Exception("vswhere.exe invalid checksum")

    def package(self):
        self.copy("LICENSE.txt", dst=self.package_folder)
        self.copy("vswhere.exe", dst=self.package_folder)

    def package_info(self):
        self.env_info.PATH.append(self.package_folder)

