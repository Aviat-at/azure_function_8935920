import azure.functions as func

app = func.FunctionApp()

@app.route(route="HttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name')
    return func.HttpResponse(f"Hello, {name if name else 'World'}!")