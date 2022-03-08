const titleInput = document.querySelector("input[name=title]");
const slugInput = document.querySelector("input[name=slug");

const slugify = (val) => {
  return val
    .toString()
    .trim()
    .toLowerCase()
    .replace(/\s+/g, "-")
    .replace(/[^\w\u0621-\u064A0-9-گدٔچپژک ٓی]+/g, "")
    .replace(/\-\-+/g, "-")
    .replace(/^-+/g, "")
    .replace(/-+$/g, "")
    .replace(/x/g, "")
    .replace(/x/g, "");
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.value = "";
  slugInput.value = slugify(titleInput.value);
});
