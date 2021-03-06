FROM python:3.7.0

RUN mkdir app
ADD server/src /app

ADD server/requirements.txt /app/requirements.txt
# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app
# Install any needed packages specified in requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

# Run app.py when the container launches

# CMD python app/flask_app.py

ENTRYPOINT [ "python" ] 
CMD [ "app.py" ]