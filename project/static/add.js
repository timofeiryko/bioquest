const addQuImageFormBtn = document.querySelector("#add-quimage-form");

const quimageForm = document.getElementsByClassName("quimage-form");
const mainForm = document.querySelector("#form");

const totalForms = document.querySelector("#id_quimage-TOTAL_FORMS");

let formCount = quimageForm.length - 1;

addQuImageFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newQuImageForm = quimageForm[0].cloneNode(true);

    const formRegex = RegExp(`quimage-(\\d){1}-`, 'g');
    formCount++;

    newQuImageForm.innerHTML = newQuImageForm.innerHTML.replace(formRegex, `quimage-${formCount}-`);
    mainForm.insertBefore(newQuImageForm, addQuImageFormBtn);
    totalForms.setAttribute('value', `${formCount + 1}`);
});
