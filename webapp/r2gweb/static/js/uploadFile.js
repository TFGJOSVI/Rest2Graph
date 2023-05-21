"use strict"

function updloadTypeObject() {
    const checkboxes = document.querySelectorAll('.type-atribute');
    const selects = document.querySelectorAll('.form-select');
    const textarea = document.getElementById('floatingTextarea');
    const textareatitle = document.querySelector('.modal-edit-title').textContent;
    const required = document.querySelectorAll('.required');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            const checkedCheckboxes = document.querySelectorAll('.type-atribute:checked');
            const attributes = [];
            attributes.push(textareatitle + '{');

            checkboxes.forEach(checkbox => {
                const select = document.querySelector(`#select-${checkbox.id}`);
                const type = select.options[select.selectedIndex].textContent;
                const req = document.querySelector(`#required-${checkbox.id}`);
                const reqLabel = document.querySelector(`#required-label-${checkbox.id}`);

                if (checkbox.checked) {
                    if (type == 'ID') {
                        req.style.display = 'none';
                        reqLabel.style.display = 'none';
                    } else {
                        req.style.display = 'block';
                        reqLabel.style.display = 'block';
                    }
                    select.style.display = 'block';
                    select.parentNode.style.display = 'block';
                } else {
                    req.style.display = 'none';
                    reqLabel.style.display = 'none';
                    select.style.display = 'none';
                    select.parentNode.style.display = 'none';
                }
            });

            checkedCheckboxes.forEach(checked => {
                const label = document.querySelector(`[for="${checked.id}"]`).textContent;
                const select = document.querySelector(`#select-${checked.id}`);
                const type = select.options[select.selectedIndex].textContent;
                const required = document.querySelector(`#required-${checked.id}`);
                const reqLabel = document.querySelector(`#required-label-${checked.id}`);

                if(type == 'ID'){
                    required.checked = true;
                }else{
                    required.checked = false;
                }

                if (required.checked) {
                    attributes.push(`\t${label}: ${type}!`);
                } else {
                    attributes.push(`\t${label}: ${type}`);
                }

            });


            attributes.push('}');
            textarea.value = attributes.join('\n');
        });
    });

    selects.forEach(select => {
        select.addEventListener('change', () => {
            const checkedCheckboxes = document.querySelectorAll('.type-atribute:checked');
            const attributes = [];
            attributes.push(textareatitle + '{');

            checkboxes.forEach(checkbox => {
                const select = document.querySelector(`#select-${checkbox.id}`);
                const type = select.options[select.selectedIndex].textContent;
                const req = document.querySelector(`#required-${checkbox.id}`);
                const reqLabel = document.querySelector(`#required-label-${checkbox.id}`);

                if (checkbox.checked) {
                    if (type == 'ID') {
                        req.style.display = 'none';
                        reqLabel.style.display = 'none';
                    } else {
                        req.style.display = 'block';
                        reqLabel.style.display = 'block';
                    }
                    select.style.display = 'block';
                    select.parentNode.style.display = 'block';
                } else {
                    req.style.display = 'none';
                    reqLabel.style.display = 'none';
                    select.style.display = 'none';
                    select.parentNode.style.display = 'none';
                }
            });


            checkedCheckboxes.forEach(checked => {
                const label = document.querySelector(`[for="${checked.id}"]`).textContent;
                const select = document.querySelector(`#select-${checked.id}`);
                const type = select.options[select.selectedIndex].textContent;
                const required = document.querySelector(`#required-${checked.id}`);
                const reqLabel = document.querySelector(`#required-label-${checked.id}`);

                if(type == 'ID'){
                        required.checked = true;
                }else{
                    required.checked = false;
                }

                if (required.checked) {
                    attributes.push(`\t${label}: ${type}!`);
                } else {
                    attributes.push(`\t${label}: ${type}`);
                }

            });
            attributes.push('}');
            textarea.value = attributes.join('\n');
        });

        required.forEach(req => {
            req.addEventListener('change', () => {
                const checkedCheckboxes = document.querySelectorAll('.type-atribute:checked');
                const attributes = [];
                attributes.push(textareatitle + '{');

                checkboxes.forEach(checkbox => {
                    const select = document.querySelector(`#select-${checkbox.id}`);
                    const type = select.options[select.selectedIndex].textContent;
                    const req = document.querySelector(`#required-${checkbox.id}`);
                    const reqLabel = document.querySelector(`#required-label-${checkbox.id}`);

                    if (checkbox.checked) {
                        if (type == 'ID') {
                            req.style.display = 'none';
                            reqLabel.style.display = 'none';
                        } else {
                            req.style.display = 'block';
                            reqLabel.style.display = 'block';
                        }
                        select.style.display = 'block';
                        select.parentNode.style.display = 'block';
                    } else {
                        req.style.display = 'none';
                        reqLabel.style.display = 'none';
                        select.style.display = 'none';
                        select.parentNode.style.display = 'none';
                    }
                });

                checkedCheckboxes.forEach(checked => {
                    const label = document.querySelector(`[for="${checked.id}"]`).textContent;
                    const select = document.querySelector(`#select-${checked.id}`);
                    const type = select.options[select.selectedIndex].textContent;
                    const required = document.querySelector(`#required-${checked.id}`);
                    const reqLabel = document.querySelector(`#required-label-${checked.id}`);

                    if(type == 'ID'){
                        required.checked = true;
                    }

                    if (required.checked) {
                        attributes.push(`\t${label}: ${type}!`);

                    } else {
                        attributes.push(`\t${label}: ${type}`);
                    }

                });
                attributes.push('}');
                textarea.value = attributes.join('\n');

            });
        });


    });
}

// Esta función carga inicalmente en el textarea el tipo de objeto con sus atributos seleccionados
function loadTypeObject(){
    const checkboxes = document.querySelectorAll('.type-atribute');
    const selects = document.querySelectorAll('.form-select');
    const textarea = document.getElementById('floatingTextarea');
    const textareatitle = document.querySelector('.modal-edit-title').textContent;
    const required = document.querySelectorAll('.required');

    const checkedCheckboxes = document.querySelectorAll('.type-atribute:checked');
    const attributes = [];
    attributes.push(textareatitle+'{');

    checkboxes.forEach(checkbox => {
        const select = document.querySelector(`#select-${checkbox.id}`);
        const type = select.options[select.selectedIndex].textContent;
        const req = document.querySelector(`#required-${checkbox.id}`);
        const reqLabel = document.querySelector(`#required-label-${checkbox.id}`);

        if (checkbox.checked) {
            if(type == 'ID'){
                req.style.display = 'none';
                reqLabel.style.display = 'none';
            }else{
                req.style.display = 'block';
                reqLabel.style.display = 'block';
            }
            select.style.display = 'block';
            select.parentNode.style.display = 'block';
        } else {
            req.style.display = 'none';
            reqLabel.style.display = 'none';
            select.style.display = 'none';
            select.parentNode.style.display = 'none';
        }
    });

    checkedCheckboxes.forEach(checked => {
      const label = document.querySelector(`[for="${checked.id}"]`).textContent;
      const select = document.querySelector(`#select-${checked.id}`);
      const type = select.options[select.selectedIndex].textContent;
      const req = document.querySelector(`#required-${checked.id}`);

        if(type == 'ID'){
            req.checked = true;
        }

        if (req.checked) {
            attributes.push(`\t${label}: ${type}!`);
        } else {
            attributes.push(`\t${label}: ${type}`);
        }


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