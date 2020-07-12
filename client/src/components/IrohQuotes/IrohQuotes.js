import axios from "axios";
import { waterSymbol, airSymbol, earthSymbol, fireSymbol } from '../../assets/js/elements.js'


export default {
    name: "IrohQuotes",
    data() {
        return {
            element: null,
            quote: {}
        };
    },
    created() {
        let elements = [waterSymbol, airSymbol, earthSymbol, fireSymbol]
        let i = Math.floor(Math.random() * 4)
        this.element = elements[i]

        let API = axios.create({
            baseURL: process.env.VUE_APP_BACKEND_HOST
        });
        /* Note: GET is hardcoded, for now, since it is the only type of request made */
        API.get("quotes/iroh/random").then(response => {
            this.quote = response.data;
        });
    },
    mounted() {
        this.card = document.getElementById("quote-card");
    },
    methods: {
        flipFlashcard: function() {
            this.card.classList.toggle("is-flipped");
        }
    }
};
