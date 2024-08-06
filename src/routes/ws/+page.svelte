<script>
    import { onMount } from "svelte";

    onMount(() => {
        const exampleSocket = new WebSocket("ws://localhost:8000/details");

        exampleSocket.onopen = (event) => {
            console.log("WebSocket connection opened.");
            exampleSocket.send("Here's some text that the server is urgently awaiting!");
        };

        exampleSocket.onmessage = (event) => {
            console.log("Message from server:", event.data);
        };

        exampleSocket.onclose = (event) => {
            console.log("WebSocket connection closed.");
        };

        exampleSocket.onerror = (error) => {
            console.error("WebSocket error:", error);
        };
    });
</script>

<h1>This is websocket</h1>