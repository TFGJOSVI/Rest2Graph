"use strict"

function updloadTypeObject(){
    const checkboxes = document.querySelectorAll('.type-atribute');
    const selects = document.querySelectorAll('.form-select');
    const textarea = document.getElementById('floatingTextarea');
    const textareatitle = document.querySelector('.modal-edit-title').textContent;







    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        const checkedCheckboxes = document.querySelectorAll('.type-atribute:checked');
        const attributes = [];
        attributes.push(textareatitle+'{');

        checkedCheckboxes.forEach(checked => {
          const label = document.querySelector(`[for="${checked.id}"]`).textContent;
          const select = document.querySelector(`#select-${checked.id}`);
          const type = select.options[select.selectedIndex].textContent;

          attributes.push(`\t${label}: ${type}`);
        });
        attributes.push('}');
        textarea.value = attributes.join('\n');
      });
    });

    selects.forEach(select => {
        select.addEventListener('change', () => {
            const checkedCheckboxes = document.querySelectorAll('.type-atribute:checked');
            const attributes = [];
            attributes.push(textareatitle+'{');

            checkedCheckboxes.forEach(checked => {
              const label = document.querySelector(`[for="${checked.id}"]`).textContent;
              const select = document.querySelector(`#select-${checked.id}`);
              const type = select.options[select.selectedIndex].textContent;

              attributes.push(`\t${label}: ${type}`);
            });
            attributes.push('}');
            textarea.value = attributes.join('\n');
          });
    });

}

// Esta función carga inicalmente en el textarea el tipo de objeto con sus atributos seleccionados
function loadTypeObject(){
    const checkboxes = document.querySelectorAll('.type-atribute');
    const selects = document.querySelectorAll('.form-select');
    const textarea = document.getElementById('floatingTextarea');
    const textareatitle = document.querySelector('.modal-edit-title').textContent;

    const checkedCheckboxes = document.querySelectorAll('.type-atribute:checked');
    const attributes = [];
    attributes.push(textareatitle+'{');

    checkedCheckboxes.forEach(checked => {
      const label = document.querySelector(`[for="${checked.id}"]`).textContent;
      const select = document.querySelector(`#select-${checked.id}`);
      const type = select.options[select.selectedIndex].textContent;

      attributes.push(`\t${label}: ${type}`);
    });
    attributes.push('}');
    textarea.value = attributes.join('\n');


}

function main(){
    window.addEventListener('load', () => {
      loadTypeObject();
      updloadTypeObject();
    });
}

document.addEventListener('DOMContentLoaded', main);