<template>
  <nuxt-link
    :to="`posts/${post.slug}`"
    :class="{ post: true, main: main, regular: !main }"
  >
    <img :src="post.thumbnail" :alt="post.title" />
    <div>
      <span class="date">{{ post.date }}</span>
      <h1>{{ post.title }}</h1>
      <p>{{ post.excerpt }}</p>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  props: ["post", "main"],
};
</script>

<style lang="scss" scoped>
@import "../scss/variables.scss";

a.post {
  cursor: pointer;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;

  transition: $transition;

  h1 {
    background: linear-gradient(90deg, $pink, $red, $orange);
    -webkit-text-fill-color: transparent;
    background-clip: text;

    filter: grayscale(1) brightness(0);

    transition: $transition;
  }

  img {
    border-radius: 0.5rem;
    width: 100%;
    object-fit: cover;
  }

  div {
    span {
      color: $gray;
      letter-spacing: 2px;
    }
  }

  &:hover {
    transform: scale(1.025);

    h1 {
      filter: grayscale(0) brightness(1);
    }
  }
}

a.main {
  margin: 2rem 0;

  h1 {
    margin: 1rem 0;
    font-size: 3rem;
    line-height: 3.25rem;
    letter-spacing: -2px;
  }

  @media (min-width: 900px) {
    margin: 2rem 0 4rem 0;

    flex-direction: row;

    img {
      width: 48%;
    }
  }
}

a.regular {
  gap: 1rem;

  h1 {
    margin: 0.5rem 0;
    font-size: 2rem;
    letter-spacing: -1px;
    line-height: 2.25rem;
  }
}
</style>