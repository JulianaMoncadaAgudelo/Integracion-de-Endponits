"""
Script de migración para agregar los nuevos campos al modelo Tarea.
Ejecuta este script una vez para actualizar la base de datos existente.
"""

from app import app, db, Tarea
from sqlalchemy import text

def migrate_database():
    """Agrega las nuevas columnas a la tabla Tarea si no existen"""
    with app.app_context():
        try:
            # Verificar si la tabla existe
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            
            if 'tarea' not in tables:
                print("La tabla 'tarea' no existe.")
                print("La base de datos se creara automaticamente al ejecutar app.py")
                print("No es necesario migrar. Los nuevos campos se crearan automaticamente.")
                return
            
            # Verificar si las columnas ya existen
            columns = [col['name'] for col in inspector.get_columns('tarea')]
            
            print("Columnas actuales:", columns)
            
            # Agregar columnas si no existen
            if 'category' not in columns:
                print("Agregando columna 'category'...")
                db.session.execute(text("ALTER TABLE tarea ADD COLUMN category VARCHAR(50)"))
                print("[OK] Columna 'category' agregada")
            else:
                print("[OK] Columna 'category' ya existe")
            
            if 'risk_analysis' not in columns:
                print("Agregando columna 'risk_analysis'...")
                db.session.execute(text("ALTER TABLE tarea ADD COLUMN risk_analysis TEXT"))
                print("[OK] Columna 'risk_analysis' agregada")
            else:
                print("[OK] Columna 'risk_analysis' ya existe")
            
            if 'risk_mitigation' not in columns:
                print("Agregando columna 'risk_mitigation'...")
                db.session.execute(text("ALTER TABLE tarea ADD COLUMN risk_mitigation TEXT"))
                print("[OK] Columna 'risk_mitigation' agregada")
            else:
                print("[OK] Columna 'risk_mitigation' ya existe")
            
            db.session.commit()
            print("\n[OK] Migracion completada exitosamente")
            
        except Exception as e:
            db.session.rollback()
            print(f"\n[ERROR] Error durante la migracion: {str(e)}")
            print("\nNota: Si la base de datos no existe, se creara automaticamente al ejecutar app.py")
            # No hacer raise, solo informar

if __name__ == '__main__':
    print("Iniciando migración de base de datos...")
    print("=" * 50)
    migrate_database()

