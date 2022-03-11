const titleInput = document.querySelector("input[name=title]");
const slugInput = document.querySelector("input[name=slug]");
const imageFile = document.getElementById("id_image");
const imageLabel = document.getElementById("upload_label");

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
    .replace(/x/g, "")
    .slice(0, 50);
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.value = "";
  slugInput.value = slugify(titleInput.value);
});

imageFile.addEventListener("change", function () {
  const name = imageFile.value.replace(/^.*[\\\/]/, "");
  if (name) {
    imageLabel.textContent = name;
    imageLabel.className = "btn btn-success";
  } else {
    imageLabel.textContent = "برای انتخاب عکس کلیک کن";
    imageLabel.className = "btn btn-secondary";
  }
});
