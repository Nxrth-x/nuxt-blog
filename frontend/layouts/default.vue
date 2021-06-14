<template>
  <div class="page-wrapper">
    <Nuxt />
  </div>
</template>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap");
@import "../scss/variables.scss";

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

html,
body {
  background: $background;
  color: $gray-dark;
}

h1,
h2,
h3,
h4,
h5,
h6,
strong,
b {
  color: $black;
}

a {
  color: inherit;
  text-decoration: none;
}

img {
  width: 100%;
}

button {
  cursor: pointer;
}

div.page-wrapper {
  min-height: 100vh;

  background: url("../static/bgcircle.svg");
  background-size: auto;
}

.container {
  max-width: 70rem;
  width: 90%;

  margin: 0 auto;
}

@media (max-width: 1080px) {
  html {
    font-size: 93.75%;
  }
}

@media (max-width: 720px) {
  html {
    font-size: 87.5%;
  }
}

@media (max-width: 600px) {
  html {
    font-size: 81.25%;
  }
}
</style>
