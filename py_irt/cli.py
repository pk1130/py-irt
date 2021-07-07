from typing import Optional, List
from py_irt.io import write_json
import typer
import time
from pathlib import Path
from rich.console import Console
from py_irt.training import IrtModelTrainer
from py_irt.config import IrtConfig


console = Console()
app = typer.Typer()


@app.command()
def train(
    model_type: str,
    data_path: str,
    output_dir: str,
    epochs: int = 2000,
    device: str = "cpu",
    initializers: Optional[List[str]] = None,
):
    console.log(f"model_type: {model_type} data_path: {model_type}")
    start_time = time.time()
    config = IrtConfig(model_type=model_type, epochs=epochs, initializers=initializers)
    trainer = IrtModelTrainer(config=config, data_path=data_path)
    output_dir = Path(output_dir)
    console.log("Training Model...")
    trainer.train(device=device)
    trainer.save(output_dir / "parameters.json")
    write_json(output_dir / "best_parameters.json", trainer.best_params)
    end_time = time.time()
    elapsed_time = end_time - start_time
    console.log("Train time:", elapsed_time)


@app.command()
def evaluate():
    raise NotImplementedError()


if __name__ == "__main__":
    app()
