from conans import ConanFile

class UE4LibConan(ConanFile):
    name = "ue4lib"
    version = "ue4"
    exports = "*.py"
    build_policy = "missing"
    
    def package(self):
        self.copy("*.py")
    
    def package_info(self):
        self.env_info.PYTHONPATH.append(self.package_folder)
