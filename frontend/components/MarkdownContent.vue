<template>
  <div>
    <h2 class="markdown-excerpt">{{ excerpt }}</h2>
    <div class="markdown-content-wrapper" v-html="rendered" />
  </div>
</template>

<script>
export default {
  props: ["content", "excerpt"],
  data() {
    return {
      rendered: this.$md.render(this.content),
    };
  },
};
</script>

<style lang="scss">
@import "../scss/variables.scss";

h2.markdown-excerpt {
  margin: 2rem auto;

  width: 100%;
  max-width: 50rem;

  font-size: 2rem;
  letter-spacing: -2px;
  font-weight: 500;
}

div.markdown-content-wrapper {
  margin: 2rem auto 4rem auto;

  width: 100%;
  max-width: 50rem;

  font-size: 1.25rem;
  color: $gray-dark;

  & > * {
    margin: 1.5rem 0;
  }

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-weight: 600;
    letter-spacing: -2px;
  }

  h1 {
    font-size: 3rem;
  }

  h2 {
    font-size: 2.75rem;
  }

  h3 {
    font-size: 2.5rem;
  }

  h4 {
    font-size: 2.25rem;
  }

  strong {
    color: $black;
  }

  img {
    margin: 1rem 0;

    align-self: center;

    width: 10rem;
  }

  ul {
    margin-left: 1.5rem;
  }

  code {
    padding: 0.125rem 0.25rem;

    border-radius: 0.125rem;

    font-size: 0.9rem;

    background: rgba(108, 117, 125, 0.25);
  }

  pre {
    overflow: auto;
    padding: 1rem;

    border-radius: 0.5rem;

    background: rgba(108, 117, 125, 0.25);

    code {
      background: transparent;

      font-size: 1rem;
      letter-spacing: 0.5px;
      color: $black;
    }
  }

  a {
    color: $red;
    transition: $transition;

    &:hover {
      color: $pink;
    }
  }
}
</style>