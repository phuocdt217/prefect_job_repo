from prefect import flow, task

@task
def say_hello():
    print("Hello, World!")

@flow
def my_flow():
    say_hello()

if __name__ == "__main__":
    main.serve(name="my-flow")