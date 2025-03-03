FROM python:3.9-slim-buster
WORKDIR /home
COPY scripts /home/scripts
COPY data /home/data

# Add these lines for debugging:
RUN ls -l /home/
RUN ls -l /home/scripts/

CMD ["sh", "-c", "python scripts.py & tail -f /dev/null"]