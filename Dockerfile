FROM python:3.9
WORKDIR /Inventory-classes-with-pytest-and-pdoc
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD pytest