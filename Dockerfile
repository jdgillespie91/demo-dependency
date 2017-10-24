FROM python:3.6-alpine

COPY dependency /workspace/dependency/
COPY setup.py /workspace
WORKDIR /workspace

RUN pip install -e .

# Running with one worker is important; the application uses global state (barbarism, I know).
ENTRYPOINT ["gunicorn", "-w", "1", "-b", "0.0.0.0:4000", "dependency.app:app"]
