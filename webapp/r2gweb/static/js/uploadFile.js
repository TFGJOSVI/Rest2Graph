"use strict"

function updloadTypeObject() {
    const checkboxes = document.querySelectorAll('.type-atribute');
    const selects = document.querySelectorAll('.form-select');
    const textareas = document.querySelectorAll('textarea');
    const textareatitles = document.querySelectorAll('.modal-edit-title');
    const required = document.querySelectorAll('.required');
    const schemanames = document.querySelectorAll('.schema-name');



    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', () => {
            const modal = checkbox.closest('.modal');
            const textarea = modal.querySelector('textarea');
            const textareatitle = modal.querySelector('.modal-edit-title').textContent;
            const checkedCheckboxes = modal.querySelectorAll('.type-atribute:checked');
            const schemaname = modal.querySelector('.schema-name').value;

            const attributes = [];
            attributes.push('Type'+ schemaname + '{');

            const modalcheckboxes = modal.querySelectorAll('.type-atribute');

            modalcheckboxes.forEach((checkbox) => {
                const select = modal.querySelector(`#select-${checkbox.id}`);
                const type = select.options[select.selectedIndex].textContent;
                const req = modal.querySelector(`#required-${checkbox.id}`);
                const reqLabel = modal.querySelector(`#required-label-${checkbox.id}`);

                if (checkbox.checked) {
                    req.style.display = 'block';
                    reqLabel.style.display = 'block';
                    select.style.display = 'block';
                    select.parentNode.style.display = 'block';
                } else {
                    req.style.display = 'none';
                    reqLabel.style.display = 'none';
                    select.style.display = 'none';
                    select.parentNode.style.display = 'none';
                }
            });

            checkedCheckboxes.forEach((checked) => {
              const label = modal.querySelector(`[for="${checked.id}"]`).textContent;
              const select = modal.querySelector(`#select-${checked.id}`);
              const type = select.options[select.selectedIndex].textContent;
              const req = modal.querySelector(`#required-${checked.id}`);

              if (type == 'ID') {
                req.checked = true;
              } else {
                req.checked = false;
              }

              if (req.checked) {
                attributes.push(`\t${label}: ${type}!`);
              } else {
                attributes.push(`\t${label}: ${type}`);
              }
            });

            attributes.push('}');
            textarea.value = attributes.join('\n');
        });
    });

    selects.forEach((select) => {
        select.addEventListener('change', () => {
            const modal = select.closest('.modal');
            const textarea = modal.querySelector('textarea');
            const textareatitle = modal.querySelector('.modal-edit-title').textContent;
            const checkedCheckboxes = modal.querySelectorAll('.type-atribute:checked');
            const schemaname = modal.querySelector('.schema-name').value;

            const attributes = [];
            attributes.push('Type'+ schemaname + '{');

            checkedCheckboxes.forEach((checked) => {
              const label = modal.querySelector(`[for="${checked.id}"]`).textContent;
              const select = modal.querySelector(`#select-${checked.id}`);
              const type = select.options[select.selectedIndex].textContent;
              const req = modal.querySelector(`#required-${checked.id}`);

              if (req.checked) {
                attributes.push(`\t${label}: ${type}!`);
              } else {
                attributes.push(`\t${label}: ${type}`);
              }
            });

            attributes.push('}');
            textarea.value = attributes.join('\n');
        });
    });

    required.forEach((req) => {
        req.addEventListener('change', () => {
            const modal = req.closest('.modal');
            const textarea = modal.querySelector('textarea');
            const textareatitle = modal.querySelector('.modal-edit-title').textContent;
            const checkedCheckboxes = modal.querySelectorAll('.type-atribute:checked');
            const schemaname = modal.querySelector('.schema-name').value;

            const attributes = [];
            attributes.push('Type'+ schemaname + '{');

            checkedCheckboxes.forEach((checked) => {
              const label = modal.querySelector(`[for="${checked.id}"]`).textContent;
              const select = modal.querySelector(`#select-${checked.id}`);
              const type = select.options[select.selectedIndex].textContent;
              const req = modal.querySelector(`#required-${checked.id}`);

              if (req.checked) {
                attributes.push(`\t${label}: ${type}!`);
              } else {
                attributes.push(`\t${label}: ${type}`);
              }
            });

            attributes.push('}');
            textarea.value = attributes.join('\n');
        });
    });

    schemanames.forEach((schemaname) => {
        schemaname.addEventListener('input', () => {
            const modal = schemaname.closest('.modal');
            const textarea = modal.querySelector('textarea');
            const textareatitle = modal.querySelector('.modal-edit-title').textContent;
            const checkedCheckboxes = modal.querySelectorAll('.type-atribute:checked');

            const attributes = [];
            attributes.push('Type'+ schemaname.value + '{');

            checkedCheckboxes.forEach((checked) => {
              const label = modal.querySelector(`[for="${checked.id}"]`).textContent;
              const select = modal.querySelector(`#select-${checked.id}`);
              const type = select.options[select.selectedIndex].textContent;
              const req = modal.querySelector(`#required-${checked.id}`);

              if (req.checked) {
                attributes.push(`\t${label}: ${type}!`);
              } else {
                attributes.push(`\t${label}: ${type}`);
              }
            });

            attributes.push('}');
            textarea.value = attributes.join('\n');
        });
    });


}




// Esta función carga inicalmente en el textarea el tipo de objeto con sus atributos seleccionados
function loadTypeObject() {
  const modals = document.querySelectorAll('.modal-schemas');
  modals.forEach((modal) => {
    const textarea = modal.querySelector('textarea');
    const textareatitle = modal.querySelector('.modal-edit-title').textContent;
    const checkboxes = modal.querySelectorAll('.type-atribute:checked');
    const selects = modal.querySelectorAll('.form-select');
    const required = modal.querySelectorAll('.required');
    const schemaname = modal.querySelector('.schema-name').value;



    const attributes = [];
    attributes.push('Type'+ schemaname + '{');

    const index = 1;
    checkboxes.forEach((checkbox) => {
      const label = modal.querySelector(`[for="${checkbox.id}"]`).textContent;
      const select = modal.querySelector(`#select-${checkbox.id}`);
      const type = select.options[select.selectedIndex].textContent;
      const req = modal.querySelector(`#required-${checkbox.id}`);

      if (req.checked) {
        attributes.push(`\t${label}: ${type}!`);
      } else {
        attributes.push(`\t${label}: ${type}`);
      }
    });

    attributes.push('}');
    textarea.value = attributes.join('\n');
  });
}








function main(){
    window.addEventListener('load', () => {
      loadTypeObject();
      updloadTypeObject();
    });
}

document.addEventListener('DOMContentLoaded', main);