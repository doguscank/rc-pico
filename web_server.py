def webpage():
    html = """
    <!DOCTYPE html>
    <html>
    <body>

    <form id="lightOnForm" action="./lighton">
        <input type="submit" value="Light on" />
    </form>

    <form id="lightOffForm" action="./lightoff">
        <input type="submit" value="Light off" />
    </form>

    <script>
        // Function to handle keypress events
        document.addEventListener('keypress', function(event) {
            if (event.key === 'o' || event.key === 'O') {
                // Trigger the light on form submission
                document.getElementById('lightOnForm').submit();
            } else if (event.key === 'p' || event.key === 'P') {
                // Trigger the light off form submission
                document.getElementById('lightOffForm').submit();
            }
        });
    </script>

    </body>
    </html>
    """
    
    return str(html)

def serve(connection, func):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            func(True)
        elif request =='/lightoff?':
            func(False)
        html = webpage()
        client.send(html)
        client.close()