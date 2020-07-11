<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <h3>{{ quote.body }}</h3>
        <h4>{{ quote.author }}</h4>
        <div class="flashcard__scene">
            <div id="quote-card" class="flashcard" @click="flipFlashcard">
                <div class="flashcard__face flashcard__face--front">
                    <div class="symbol-container">
                        <i class="symbol" v-html="water"></i>
                    </div>
                </div>
                <div class="flashcard__face flashcard__face--back"></div>
            </div>
        </div>
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
            water: `<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 viewBox="0 0 350 350"
 preserveAspectRatio="xMidYMid meet">
<g transform="translate(0.000000,350.000000) scale(0.100000,-0.100000)" stroke="none">
<path d="M1675 3434 c-283 -33 -505 -91 -729 -193 -268 -122 -571 -441 -741
-781 -60 -119 -89 -203 -121 -350 -22 -99 -26 -148 -31 -355 -8 -326 11 -451
106 -708 133 -363 455 -673 835 -806 274 -96 684 -160 951 -148 277 13 440 61
707 208 181 100 370 264 480 419 144 203 262 527 304 840 23 169 23 416 0 540
-71 393 -202 669 -428 906 -187 195 -449 335 -737 394 -160 32 -460 49 -596
34z m560 -164 c218 -47 351 -112 445 -217 86 -95 140 -241 140 -375 0 -63 -5
-84 -30 -135 -34 -67 -105 -140 -170 -173 -79 -40 -212 -36 -317 10 -41 18
-43 21 -43 60 0 55 -26 179 -54 256 l-23 62 25 31 c50 65 174 105 258 82 58
-16 129 -66 148 -105 9 -20 16 -60 16 -96 0 -54 -3 -65 -29 -90 -39 -40 -72
-46 -117 -23 -49 24 -59 53 -32 89 16 20 19 30 11 43 -17 27 -41 24 -74 -9
-28 -28 -31 -36 -26 -75 6 -59 30 -93 80 -116 104 -47 210 -7 258 96 25 54 25
175 0 230 -24 53 -99 121 -169 152 -115 53 -264 24 -353 -67 l-47 -48 -48 61
c-64 80 -197 186 -288 230 -86 43 -243 84 -358 95 l-83 8 115 22 c63 11 129
23 145 26 17 2 140 3 275 1 206 -3 261 -7 345 -25z m-726 -165 c189 -36 291
-88 416 -210 126 -124 187 -265 202 -465 11 -157 -31 -271 -138 -378 -33 -32
-83 -72 -112 -88 -48 -27 -59 -29 -157 -28 -96 0 -112 3 -190 35 l-84 35 -17
81 c-9 45 -31 123 -48 173 l-33 90 28 48 c79 136 131 167 268 160 72 -4 92 -9
133 -34 98 -61 154 -244 97 -321 -26 -36 -79 -63 -123 -63 -38 0 -101 54 -101
88 0 30 10 52 25 52 7 0 18 7 25 15 10 12 10 18 0 30 -32 38 -120 -28 -120
-91 0 -46 32 -107 72 -135 39 -28 128 -37 183 -19 51 17 117 85 133 136 41
140 -16 314 -130 392 -63 43 -112 56 -213 56 -128 0 -183 -21 -260 -98 -34
-34 -69 -72 -78 -85 l-16 -24 -38 34 c-58 52 -100 75 -203 110 -213 71 -425
46 -596 -72 -25 -17 -47 -29 -50 -27 -6 6 105 166 174 250 133 163 332 326
419 343 124 24 426 30 532 10z m1540 -363 c100 -148 191 -352 217 -487 6 -33
5 -37 -10 -32 -116 45 -289 53 -472 22 -226 -39 -367 -97 -524 -216 -91 -69
-162 -128 -480 -398 -213 -181 -292 -237 -425 -301 -202 -97 -327 -130 -503
-130 -182 0 -363 45 -549 137 l-112 55 -7 55 c-3 30 -4 159 -1 286 6 235 13
291 58 457 l21 80 105 71 c193 128 283 163 428 163 97 0 197 -24 286 -69 69
-36 133 -112 168 -203 97 -252 77 -476 -56 -640 -76 -93 -172 -126 -347 -120
-131 5 -190 26 -254 91 -85 87 -116 232 -72 335 29 67 103 135 172 158 122 40
259 -13 301 -116 40 -97 26 -182 -35 -220 -64 -39 -113 -24 -154 45 -27 46
-59 60 -70 30 -9 -22 46 -125 78 -149 41 -29 125 -33 175 -8 85 44 118 112
111 231 -10 170 -109 280 -279 312 -177 32 -366 -100 -415 -290 -28 -112 1
-260 73 -368 78 -117 186 -163 386 -163 116 0 204 18 280 56 64 33 171 139
215 216 36 62 82 186 82 223 l0 24 78 -37 c73 -35 83 -37 192 -40 98 -3 123
-1 171 17 185 70 332 247 374 453 l5 27 43 -19 c64 -28 159 -43 235 -38 179
13 350 175 383 365 13 73 -1 204 -31 293 l-18 55 56 -60 c31 -33 86 -102 121
-153z m184 -613 l65 -12 11 -74 c6 -41 11 -107 11 -147 l0 -73 -187 0 c-151 1
-202 -3 -258 -18 -99 -26 -210 -74 -334 -146 -122 -72 -186 -119 -441 -329
-241 -198 -449 -354 -544 -409 -164 -93 -360 -140 -621 -148 -195 -6 -283 4
-440 50 -76 21 -82 25 -113 72 -51 75 -142 285 -142 326 0 4 39 -12 88 -37
140 -71 362 -124 522 -124 177 0 388 57 589 160 145 74 220 130 543 406 416
356 506 415 709 468 205 54 380 65 542 35z m82 -446 c-2 -21 -9 -78 -15 -128
-10 -84 -28 -170 -51 -241 l-9 -30 -143 0 c-136 0 -145 -2 -222 -32 -44 -17
-127 -58 -185 -90 -213 -119 -275 -166 -495 -382 -115 -113 -239 -227 -275
-254 -123 -93 -289 -156 -520 -197 -140 -25 -173 -22 -332 31 -138 46 -238 96
-348 176 -87 62 -204 169 -175 158 149 -53 176 -58 355 -57 199 1 342 21 506
74 214 67 343 155 889 603 363 298 599 399 948 405 l77 1 -5 -37z m-105 -492
c0 -20 -54 -159 -87 -226 -62 -123 -125 -208 -232 -315 -125 -124 -227 -195
-411 -284 -252 -121 -356 -142 -675 -133 -115 4 -228 10 -250 14 -38 8 -35 9
54 22 269 38 336 78 666 402 171 167 233 221 332 287 128 86 277 168 353 196
97 35 250 58 250 37z"/>
</g>
</svg>`
        };
    },
    created() {
        let API = axios.create({
            baseURL: process.env.VUE_APP_BACKEND_HOST
        });
        /* Note: GET is hardcoded, for now, since it is the only type of request made */
        API.get("quotes/random").then(response => {
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
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
@mixin flashcard-scene($width, $height, $perspective) {
    width: $width;
    height: $height;
    perspective: $perspective;
    margin: 40px auto;
}

@mixin flashcard {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 1s;
    transform-style: preserve-3d;
    cursor: pointer;
}

/* Rotate along Y-axis and support all browsers */
@mixin rotateY-axis($degrees) {
    transform: rotateY($degrees);
    -ms-transform: rotateY($degrees);
    -webkit-transform: rotateY($degrees);
    -moz-transform: rotateY($degrees);
    -o-transform: rotateY($degrees);
}

/* Rotate along X-axis and support all browsers */
@mixin rotateX-axis($degrees) {
    transform: rotateX($degrees);
    -ms-transform: rotateX($degrees);
    -webkit-transform: rotateX($degrees);
    -moz-transform: rotateX($degrees);
    -o-transform: rotateX($degrees);
}

/* Rotate along X-axis and support all browsers */
@mixin rotateZ-axis($degrees) {
    transform: rotateZ($degrees);
    -ms-transform: rotateZ($degrees);
    -webkit-transform: rotateZ($degrees);
    -moz-transform: rotateZ($degrees);
    -o-transform: rotateZ($degrees);
}

@mixin rotate3D($x, $y, $z, $degrees) {
    transform: rotate3d($x, $y, $z, $degrees);
    -ms-transform: rotate3d($x, $y, $z, $degrees);
    -webkit-transform: rotate3d($x, $y, $z, $degrees);
    -moz-transform: rotate3d($x, $y, $z, $degrees);
    -o-transform: rotate3d($x, $y, $z, $degrees);
}

/* Hide the back face of the card when turned around, need for safari support */
@mixin backfaceVisibility() {
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
}

$rotate-degrees: 180deg;
$card-color: #e7cda7;
$font-color: #b52020;
$divider-color: #967560;

$text-margin: 18.5px;
$card-size: 400px;
$perspective: 600px;

.flashcard__scene {
    @include flashcard-scene(280px, $card-size, $perspective);

    .flashcard {
        @include flashcard();
    }

    .flashcard.is-flipped {
        @include rotateY-axis($rotate-degrees);
    }

    .flashcard__face {
        color: $font-color;
        background-color: $card-color;
        border-radius: 10px;
        border: 2px solid black;

        position: absolute;
        width: 100%;
        height: 100%;

        display: flex;
        justify-content: center;
        align-items: center;
    }

    .flashcard__face--front {
        @include backfaceVisibility();

        .symbol-container {
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 10px;
            background-color: #4f1010;
            width: 180px;
            height: 180px;
        }
        .symbol svg {
            margin-top: 6px;
            fill: #a43939;
            width: 150px;
        }
    }

    .flashcard__face--back {
        @include rotateY-axis($rotate-degrees);
        @include backfaceVisibility();

        background-color: rgb(141, 38, 38);
        // background-color: rgb(184, 46, 46);
    }
}

.hello {
    color: white;
}

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
