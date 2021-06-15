<template>
  <div>
    <Header />
    <main class="container">
      <h1 class="title">{{ post.title }}</h1>
      <ProfileInfo />
      <MarkdownContent :content="post.content" :excerpt="post.excerpt" />
      <div class="like">
        <p>{{ post.likes }}</p>
        <button @click="handleClick">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5"
            />
          </svg>
        </button>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
export default {
  async asyncData({ $axios, params, error }) {
    try {
      const post = await $axios.$get(`post/${params.slug}`);

      return {
        post,
      };
    } catch (err) {
      console.log(err);
      error("Page not found. :(");
    }
  },
  methods: {
    async handleClick() {
      const { slug } = this.$route.params;
      const axios = this.$axios;

      try {
        await axios.$post(`post/${slug}/like`);
        this.post.likes++;
      } catch {}
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/scss/variables.scss";

h1.title {
  margin: 2rem 0;

  font-size: 6rem;
  letter-spacing: -2px;
  line-height: 6.5rem;

  @media (max-width: 720px) {
    font-size: 4rem;
    line-height: 4.5rem;
  }
}

div.like {
  margin: 2rem auto 4rem auto;

  display: flex;
  align-items: center;
  flex-direction: column;

  p {
    font-size: 1.25rem;
    color: $red;
  }

  button {
    width: 3.25rem;
    height: 3.25rem;

    background: transparent;

    display: grid;
    place-items: center;

    border-radius: 50%;
    border: 1px solid $red;

    transition: $transition;

    svg {
      width: 50%;

      color: $red;

      transition: $transition;
    }
  }
}
</style>