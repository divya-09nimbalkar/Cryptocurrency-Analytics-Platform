from src.utils import log_message

def test_logger_output(capsys):
    log_message("Hello World")
    captured = capsys.readouterr()
    assert "Hello World" in captured.out
