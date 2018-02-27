from conans import ConanFile


class TestFindWindowsSigntool(ConanFile):

    def test(self):
        self.run("vswhere.exe -help")

