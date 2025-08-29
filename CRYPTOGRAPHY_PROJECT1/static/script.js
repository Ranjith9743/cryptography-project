function copyResult() {
  const text = document.querySelector(".result-box").innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert("Result copied to clipboard!");
  });
}
