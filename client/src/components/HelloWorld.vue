<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <h4>{{ firstQuote.body }}</h4>
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
            firstQuote: {}
        };
    },
    created() {
        let API = axios.create({
            baseURL: process.env.VUE_APP_BACKEND_HOST
        });
        /* Note: GET is hardcoded, for now, since it is the only type of request made */
        API.get("quote/1").then(response => {
            this.firstQuote = response.data;
        });
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>
