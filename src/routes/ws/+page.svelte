<script>
    import { onMount,onDestroy } from "svelte";
    let message;
    let socket;
    let messagelog = [];
    let replylog = [];
    onMount(() => {
        socket = new WebSocket("ws://localhost:8000/details");

        socket.onopen = (event) => {
        };

        socket.onmessage = (event) => {
            replylog = [...replylog, event.data];
        };

        socket.onclose = (event) => {
            console.log("WS Closed:", event);
        };

        socket.onerror = (error) => {
            console.error("Error:", error);
        };
    });
    onDestroy(()=>{
        socket.close();
    })
    function sendMessage() {
        if (socket && message) {
            messagelog = [...messagelog, message];
            socket.send(message);
        }
    }
</script>

<h1>Message With Yourself</h1>
<input
    type="text"
    name=""
    id=""
    placeholder="Enter Message"
    bind:value={message}
/>
<button on:click={sendMessage}>Send</button>
{#each messagelog as message, i}
    <div>{messagelog[i]}</div>
    <div>{replylog[i]}</div>
{/each}
