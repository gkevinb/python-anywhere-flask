import HelloWorld from "../components/HelloWorld.vue";
import IrohQuotes from "../components/IrohQuotes/IrohQuotes.vue";

export default {
    name: "App",
    components: {
        HelloWorld,
        IrohQuotes
    },
    data() {
        return {
            backendHost: process.env.VUE_APP_BACKEND_HOST
        };
    }
};