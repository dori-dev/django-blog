const titleInput = document.querySelector("input[name=title]");
const slugInput = document.querySelector("input[name=slug");

const slugify = (val) => {
  return val
    .toString()
    .trim()
    .replace(/[\s\W-]+/g, "-");
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.value = "";
  slugInput.value = slugify(titleInput.value);
});
