<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <h3>{{ quote.body }}</h3>
        <h4>{{ quote.author }}</h4>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "HelloWorld",
    props: {
        msg: String
    },
    data() {
        return {
            quote: {},
        }
    },
    created() {
        let API = axios.create({
            baseURL: process.env.VUE_APP_BACKEND_HOST
        });
        /* Note: GET is hardcoded, for now, since it is the only type of request made */
        API.get("quotes/random").then(response => {
            this.quote = response.data;
        });
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">

</style>
