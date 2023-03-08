from os import system, name

from time import sleep
import time


class TerminalClock:
    def __init__(self):
        self.tick_duration = 1.0
        self.start_tick = None

    def start(self):
        self.start_tick = time.process_time()

    def restart(self):
        self.start()

    def tick(self):
        if time.process_time() - self.start_tick >= self.tick_duration:
            self.restart()
            return True
        return False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

import typer

app = typer.Typer()
clock = TerminalClock()

@app.command()
def start(name: str):
    tock = 0
    clock.start()
    while(True):
        if clock.tick():
            tock +=1
            clear()
            typer.echo(f'tock {tock}')


if __name__ == "__main__":
    app()