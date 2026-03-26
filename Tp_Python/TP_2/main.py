import os
import shutil
from datetime import datetime
from exceptions import (EmployeeError, EmployeeNotFoundError, InvalidDepartmentError, 
                        InvalidSalaryError, FileBackupError)

# --- PARTIE 1 : Manipulation des fichiers texte ---

def load_employees(file_path):
    employees = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line:
                    continue
                try:
                    parts = clean_line.split(";")
                    if len(parts) != 4:
                        raise IndexError("Format incorrect (doit avoir 4 champs)")
                    
                    emp_id = int(parts[0])
                    name = parts[1]
                    department = parts[2]
                    salary = float(parts[3])
                    
                    employees.append({
                        "id": emp_id,
                        "name": name,
                        "department": department,
                        "salary": salary
                    })
                except (ValueError, IndexError) as e:
                    # Ignore les lignes incorrectes
                    print(f"Ligne {line_no} ignorée : {e}")
                    pass
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        raise
    return employees

def load_departments(file_path):
    departments = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
            if not content:
                raise ValueError(f"Le fichier '{file_path}' est vide.")
                
            for line in content:
                dept = line.strip()
                if dept:
                    if not dept.replace(" ", "").isalnum():
                        raise ValueError(f"Caractères invalides dans le département: {dept}")
                    departments.append(dept)
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        raise
    return departments

def find_employee_by_id(employees, emp_id):
    try:
        emp_id = int(emp_id)
    except ValueError:
        return None
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return None

def filter_by_department(employees, department):
    return [emp for emp in employees if emp["department"].lower() == department.lower()]

# --- PARTIE 2 : POO et gestion du système de fichiers ---

class EmployeeManager:
    def __init__(self, employees, departments):
        self.employees = employees
        self.departments = departments
        
    def add_employee(self, emp_id, name, department, salary):
        if department not in self.departments:
            raise InvalidDepartmentError(f"Le département '{department}' n'existe pas.")
        try:
            emp_id = int(emp_id)
            salary = float(salary)
            if salary < 0:
                raise InvalidSalaryError("Le salaire doit être positif.")
        except ValueError:
            raise EmployeeError("ID ou salaire ont un format incorrect.")
            
        if self._exists(emp_id):
            raise EmployeeError(f"L'employé avec l'ID {emp_id} existe déjà.")
            
        self.employees.append({
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        })
        
    def remove_employee(self, emp_id):
        emp_id = int(emp_id)
        if not self._exists(emp_id):
            raise EmployeeNotFoundError(f"L'employé {emp_id} n'a pas été trouvé.")
        self.employees = [emp for emp in self.employees if emp["id"] != emp_id]
        
    def update_salary(self, emp_id, new_salary):
        emp_id = int(emp_id)
        emp = find_employee_by_id(self.employees, emp_id)
        if not emp:
            raise EmployeeNotFoundError(f"L'employé {emp_id} n'a pas été trouvé.")
        try:
            new_salary = float(new_salary)
            if new_salary < 0:
                raise InvalidSalaryError("Le salaire doit être positif.")
            emp["salary"] = new_salary
        except ValueError:
            raise InvalidSalaryError("Format du salaire incorrect.")
            
    def _exists(self, emp_id):
        return any(e["id"] == emp_id for e in self.employees)
        
    def save_to_file(self, path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                for emp in self.employees:
                    f.write(f"{emp['id']};{emp['name']};{emp['department']};{emp['salary']}\n")
        except PermissionError:
            raise EmployeeError(f"Permission refusée pour écrire dans '{path}'.")

def backup_file(src_path, backup_folder):
    try:
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
            
        if not os.path.exists(src_path):
            raise FileNotFoundError(f"Le fichier source '{src_path}' n'existe pas.")
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        backup_filename = f"employees_backup_{timestamp}.txt"
        dest_path = os.path.join(backup_folder, backup_filename)
        
        shutil.copy2(src_path, dest_path)
        print(f"Backup réussi : {dest_path}")
    except PermissionError:
        raise FileBackupError("Permission refusée lors du backup.")
    except Exception as e:
        raise FileBackupError(f"Erreur inattendue : {e}")

# --- PARTIE 3 : Fichiers structurés ---

def export_csv(employees, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("id,name,department,salary\n")
            for emp in employees:
                if "id" not in emp or "name" not in emp or "department" not in emp or "salary" not in emp:
                    raise ValueError("Données d'employé incomplètes.")
                name_safe = str(emp["name"]).replace(",", " ")
                f.write(f"{emp['id']},{name_safe},{emp['department']},{emp['salary']}\n")
    except Exception as e:
        print(f"Erreur lors de l'export CSV : {e}")

def export_json(employees, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write('{\n    "employees": [\n')
            for i, emp in enumerate(employees):
                emp_id = emp.get("id", "null")
                name = str(emp.get("name", "")).replace('"', '\\"')
                dept = str(emp.get("department", "")).replace('"', '\\"')
                salary = emp.get("salary", "null")
                
                f.write('        {\n')
                f.write(f'            "id": {emp_id},\n')
                f.write(f'            "name": "{name}",\n')
                f.write(f'            "department": "{dept}",\n')
                f.write(f'            "salary": {salary}\n')
                
                if i < len(employees) - 1:
                    f.write('        },\n')
                else:
                    f.write('        }\n')
            f.write('    ]\n}\n')
    except Exception as e:
        print(f"Erreur lors de l'export JSON : {e}")

# --- PROGRAMME PRINCIPAL ---

if __name__ == "__main__":
    employees_file = "employees.txt"
    depts_file = "departments.txt"
    
    print("--- Démarrage de l'application ---")
    try:
        depts = load_departments(depts_file)
        emps = load_employees(employees_file)
    except Exception as e:
        print("Erreur critique :", e)
        exit(1)
        
    manager = EmployeeManager(emps, depts)
    
    # Tests
    try:
        manager.add_employee(1005, "Nouveau Test", "Informatique", 4000)
        manager.update_salary(1001, 4800)
    except EmployeeError as e:
        print("Erreur métier :", e)
        
    try:
        manager.save_to_file(employees_file)
        backup_file(employees_file, "backups")
    except EmployeeError as e:
        print("Erreur fichier :", e)
        
    export_csv(manager.employees, "export.csv")
    export_json(manager.employees, "export.json")
    print("Exportations terminées.")
