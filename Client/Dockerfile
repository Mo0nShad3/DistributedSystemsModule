# Stage 1: Build the base image
FROM python:3.9-slim-buster AS base

# Stage 2: Build each client image
FROM base AS builder
WORKDIR /app

COPY client_1.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_1.py

COPY client_2.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_2.py

COPY client_3.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_3.py

COPY client_4.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_4.py

COPY client_5.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_5.py

COPY client_6.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_6.py

COPY client_7.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_7.py

COPY client_8.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_8.py

COPY client_9.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_9.py

COPY client_10.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_10.py

COPY client_11.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_11.py

COPY client_12.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_12.py

COPY client_13.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_13.py

COPY client_14.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_14.py

COPY client_15.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python client_15.py

# Stage 3: Create final images
COPY --from=builder /app/client_1.py .
COPY --from=builder /app/client_2.py .
COPY --from=builder /app/client_3.py .
COPY --from=builder /app/client_4.py . 
COPY --from=builder /app/client_5.py .
COPY --from=builder /app/client_6.py .
COPY --from=builder /app/client_7.py .
COPY --from=builder /app/client_8.py . 
COPY --from=builder /app/client_9.py .
COPY --from=builder /app/client_10.py .
COPY --from=builder /app/client_11.py .
COPY --from=builder /app/client_12.py . 
COPY --from=builder /app/client_13.py . 
COPY --from=builder /app/client_14.py .
COPY --from=builder /app/client_15.py .