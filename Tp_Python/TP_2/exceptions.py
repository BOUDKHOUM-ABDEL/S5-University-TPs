class EmployeeError(Exception):
    def __init__(self, message="Erreur liée à l'employé"):
        super().__init__(message)
        self.message = message
        
    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"

class EmployeeNotFoundError(EmployeeError):
    def __init__(self, message="Employé introuvable"):
        super().__init__(message)

class InvalidDepartmentError(EmployeeError):
    def __init__(self, message="Département invalide"):
        super().__init__(message)

class InvalidSalaryError(EmployeeError):
    def __init__(self, message="Salaire invalide"):
        super().__init__(message)

class FileBackupError(EmployeeError):
    def __init__(self, message="Erreur lors de la sauvegarde du fichier"):
        super().__init__(message)
