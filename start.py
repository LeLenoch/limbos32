import threading
import subprocess

def run_server():
    subprocess.run(['python', 'server.py'])

def run_spawn_all():
    subprocess.run(['python', 'spawn-all.py'])

if __name__ == "__main__":
    # Créer les threads pour chaque programme
    server_thread = threading.Thread(target=run_server)
    spawn_all_thread = threading.Thread(target=run_spawn_all)

    # Démarrer les threads
    server_thread.start()
    spawn_all_thread.start()

    # Attendre que les threads se terminent
    server_thread.join()
    spawn_all_thread.join()
