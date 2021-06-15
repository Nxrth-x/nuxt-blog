<template>
  <footer>
    <div class="container">
      <h1>Nxrth-x</h1>
      <div class="info">
        <div class="links">
          <a href="https://facebook.com/dcclxxix" target="_blank">Facebook</a>
          <a href="https://linkedin.com/in/lima-eder" target="_blank"
            >LinkedIn</a
          >
          <a href="https://github.com/Nxrth-x" target="_blank">GitHub</a>
        </div>
        <div class="about">
          <p>
            Nxrth-x is a blog about sharing my developer experiences, technology
            and experimentation with new stuff, I hope it resonates with you.
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import "../scss/variables.scss";

footer {
  padding: 1rem 0;
  background: $black;
  color: $gray;

  h1 {
    // Fix for cutting the text
    padding-right: 1rem;
    margin: 1rem 0;

    width: fit-content;

    letter-spacing: -2px;

    background: linear-gradient(90deg, $pink, $red, $orange);
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  div.info {
    margin: 1rem 0;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 2rem;

    div.links {
      display: flex;
      flex-direction: column;

      a {
        transition: $transition;

        &:hover {
          color: $orange;
        }
      }
    }

    @media (min-width: 900px) {
      flex-direction: row;
      gap: 50%;
    }
  }
}
</style>