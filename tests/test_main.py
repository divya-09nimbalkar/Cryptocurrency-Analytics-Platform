from src.utils import log_message

def test_log_message(capsys):
    log_message("Test message")
    captured = capsys.readouterr()
    assert "Test message" in captured.out
