import sounddevice as sd
import socket

# Audio recording settings
CHUNK = 1024
CHANNELS = 2
RATE = 44100

# Networking settings
HOST = "127.0.0.1"
PORT = 12343


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)

            def callback(indata, frames, time, status):
                if status:
                    print(status, flush=True)

                data_bytes = indata.tobytes()
                conn.sendall(data_bytes)

            with sd.InputStream(channels=CHANNELS, callback=callback, dtype="int16"):
                while True:
                    pass  # Keep the program running


if __name__ == "__main__":
    start_server()
