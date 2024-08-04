<script>
    import { goto } from "$app/navigation";
</script>

<main>
    <button on:click={() => goto("/create")}>Create</button>
    <button on:click={() => goto("/join")}>Join</button>
</main>

<style lang="scss">
    main{
        font-family: 'Courier New', Courier, monospace;
        padding-left: 5px;
    }
</style>