FROM public.ecr.aws/lambda/python:3.8
COPY ./api ./api
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/api"
CMD ["api.main.handler"]