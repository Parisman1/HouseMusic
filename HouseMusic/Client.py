import socket
import pygame
import io

# Networking settings
HOST = "127.0.0.1"
PORT = 12343


def start_client():
    pygame.init()
    pygame.mixer.init()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        while True:
            try:
                s.connect((HOST, PORT))
                print(f"Connected to {HOST}:{PORT}")
                break  # Exit the loop if the connection is successful
            except ConnectionRefusedError:
                print(f"Connection refused. Retrying...")
                continue

        stream = io.BytesIO()

        while True:
            chunk = s.recv(1024)
            if not chunk:
                break

            stream.write(chunk)
            stream.seek(0)  # Move the stream position to the beginning for playback

            sound = pygame.mixer.Sound(buffer=stream.getvalue())
            pygame.mixer.Channel(0).play(sound)

            while pygame.mixer.get_busy():
                pygame.time.Clock().tick(10)

            stream.seek(0)
            stream.truncate()


if __name__ == "__main__":
    start_client()
