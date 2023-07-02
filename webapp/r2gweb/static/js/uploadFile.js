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
            attributes.push('Type' + schemaname + '{');

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
            attributes.push('Type' + schemaname + '{');

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
            attributes.push('Type' + schemaname + '{');

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
            attributes.push('Type' + schemaname.value + '{');

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
        attributes.push('Type' + schemaname + '{');

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


let indexGet = {};

let gets = {};

let indexPost = {};

let posts = {};

let indexPut = {};

let puts = {};

let indexDelete = {};

let deletes = {};

let openAPI;

function charge(oas) {
    if (openAPI === undefined) {
        console.log('---undefined---');
        openAPI = oas;
    }
}

function changeObject(type, loopIndex, oas) {


    let method = document.getElementById(`${type}s-method-name-${loopIndex}`);
    let url = document.getElementById(`gets-method-url-${loopIndex}`);

    let oldUrl = document.getElementById(`url-${type}-${loopIndex}`).textContent;
    let oldMethod = document.getElementById(`method-${type}-${loopIndex}`).textContent;

    document.getElementById(`url-${type}-${loopIndex}`).textContent = url.value;
    document.getElementById(`method-${type}-${loopIndex}`).textContent = method.value;

    if (method.value.toString().trim() !== oldMethod.toString().trim() || url.value.toString().trim() !== oldUrl.toString().trim()) {
        if (type == 'get') {
            openAPI.queries.forEach()((query) => {
                if (query.url === oldUrl && query.method === oldMethod) {
                    query.url = url.value;
                    query.method = method.value;
                }
            })
        } else {
            openAPI.mutations.forEach()((mutation) => {
                if (mutation.url === oldUrl && mutation.method === oldMethod) {
                    mutation.url = url.value;
                    mutation.method = method.value;
                }
            })
        }
    }


    if (method.value.toString().trim() !== oldMethod.toString().trim() || url.value.toString().trim() !== oldUrl.toString().trim()) {
        if (type === 'get' && !(loopIndex in indexGet)) {
            indexGet[loopIndex] = oldUrl;
        } else if (type === 'post' && !(loopIndex in indexPost)) {
            indexPost[loopIndex] = oldUrl;
        } else if (type === 'put' && !(loopIndex in indexPut)) {
            indexPut[loopIndex] = oldUrl;
        } else if (type === 'delete' && !(loopIndex in indexDelete)) {
            indexDelete[loopIndex] = oldUrl;
        }

        let o = {
            'url': url.value,
            'method': method.value,
        }

        if (type === 'get') {
            gets[loopIndex] = o;
        } else if (type === 'post') {
            posts[loopIndex] = o;
        } else if (type === 'put') {
            puts[loopIndex] = o;
        } else if (type === 'delete') {
            deletes[loopIndex] = o;
        }

    }

    let modal = document.getElementById(`${type}-edit-modal-${loopIndex}`);

    if (modal.classList.contains('show')) {
        modal.classList.remove('show');
        modal.setAttribute('aria-hidden', 'true');
        modal.style.display = 'none';
        document.body.classList.remove('modal-open');
        let modalBackdrop = document.getElementsByClassName('modal-backdrop')[0];
        document.body.removeChild(modalBackdrop);
    }

}


function changeSchema(oas, index) {

    if (openAPI === undefined) {
        console.log('---undefined---');
        openAPI = oas;
    }


    let schema = document.getElementById(`div-schema-${index}`);

    let oldName = schema.querySelector("#title-schema").textContent;

    let newName = document.querySelector(`[id^="floatingInput-schema-${index}"]`).value;

    if (oldName.trim() !== newName) {
        document.getElementById("title-schema").textContent = `Type${newName}`;
        document.querySelector(`[id^="label-schema-${index}"]`).textContent = newName;
    }

    let atributosDiv = schema.querySelector(`[id^="edit-modal-schema-${index}"]`);


    required

    let atributosObject = {
        "oldName": oldName,
        "newName": newName,
        "atributes": []
    };


    atributos.forEach((atributo) => {
        let as = atributo.querySelectorAll(`[id^="atribute"]`);

        as.forEach((a) => {


            let required = a.getElementsByClassName("required-atribute")[0].getElementsByTagName("input")[0].checked;

            let type = a.querySelector(`[id^="select-schema"]`).value;

            let o = {
                'required': required,
                'type': type,
                'name': a.querySelector('[id^="name-attribute"]').textContent,
            }

            atributosObject.atributes.push(o);

        });
    });

    let modal = document.getElementById(`edit-modal-schema-${index}`);

    if (modal.classList.contains('show')) {
        modal.classList.remove('show');
        modal.setAttribute('aria-hidden', 'true');
        modal.style.display = 'none';
        document.body.classList.remove('modal-open');
        let modalBackdrop = document.getElementsByClassName('modal-backdrop')[0];
        document.body.removeChild(modalBackdrop);
    }

    changeAllSchemasOpenAPI(atributosObject);

}

function changeAllSchemasOpenAPI(schema) {


    let nameAtributes = schema.atributes.map((a) => {
        return a.name
    });


    let u = openAPI.queries.filter((q) => {
        return q.response !== null;
    }).filter((q) => {
        return q.response.schema.component.name.trim() === schema.oldName.replace("Type", "").trim();
    });

    openAPI.queries
        .filter((q) => {
            return q.response !== null;
        })
        .filter((q) => {
            return q.response.schema.component.name.trim() === schema.oldName.replace("Type", "").trim();
        })
        .forEach((q) => {
            q.response.schema.component.name = schema.newName;
        });

    openAPI.queries
        .filter((q) => {
            return q.response !== null;
        })
        .filter((q) => {
            return q.response.schema.component.name.trim() === schema.newName;
        })
        .forEach((q) => {
            q.response.schema.component.attributes.forEach((a) => {
                console.log(a.name);
                if (nameAtributes.includes(a.name.trim())) {
                    let o = schema.atributes.find((at) => {
                        return at.name.trim() === a.name.trim();
                    });

                    if (o) {
                        a.required = o.required;
                        a.type = o.type;
                    }
                }
            });
        });

    openAPI.mutations
        .filter((q) => {
            return q.response !== null;
        })
        .filter((q) => {
            return q.response.schema.component.name.trim() === schema.oldName.replace("Type", "").trim();
        })
        .forEach((q) => {
            q.response.schema.component.name = schema.newName;
        });

    openAPI.mutations
        .filter((q) => {
            return q.request !== null;
        })
        .filter((q) => {
            return q.request.schema.component.name.trim() === schema.oldName.replace("Type", "").trim();
        })
        .forEach((q) => {
            q.request.schema.component.name = schema.newName;
        });

    openAPI.mutations
        .filter((q) => {
            return q.response !== null;
        })
        .filter((q) => {
            return q.response.schema.component.name.trim() === schema.newName;
        })
        .forEach((q) => {
            q.response.schema.component.attributes.forEach((a) => {
                console.log(a.name);
                if (nameAtributes.includes(a.name.trim())) {
                    let o = schema.atributes.find((at) => {
                        return at.name.trim() === a.name.trim();
                    });

                    if (o) {
                        a.required = o.required;
                        a.type = o.type;
                    }
                }
            });
        });

    openAPI.mutations
        .filter((q) => {
            return q.request !== null;
        })
        .filter((q) => {
            return q.request.schema.component.name.trim() === schema.newName;
        })
        .forEach((q) => {
            q.request.schema.component.attributes.forEach((a) => {
                console.log(a.name);
                if (nameAtributes.includes(a.name.trim())) {
                    let o = schema.atributes.find((at) => {
                        return at.name.trim() === a.name.trim();
                    });

                    if (o) {
                        a.required = o.required;
                        a.type = o.type;
                    }
                }
            });
        });


}

function sentOpenAPI() {

    if (openAPI === undefined) {
        openAPI = openApi;
    }

    let q = document.querySelectorAll('[id^="get-label"]');

    let queries = []

    q.forEach((query) => {
        let check = document.getElementById(query.htmlFor).checked;
        let name = query.querySelector('[id^="method-get"]').textContent;
        queries.push({'check': check, 'name': name});
    });

    let p = document.querySelectorAll('[id^="post-label"]');

    let mutations = []

    p.forEach((query) => {
        let check = document.getElementById(query.htmlFor).checked;
        let name = query.querySelector('[id^="method-post"]').textContent;
        mutations.push({'check': check, 'name': name});
    });

    let pu = document.querySelectorAll('[id^="put-label"]');


    pu.forEach((query) => {
        let check = document.getElementById(query.htmlFor).checked;
        let name = query.querySelector('[id^="method-put"]').textContent;
        mutations.push({'check': check, 'name': name});
    });

    let de = document.querySelectorAll('[id^="delete-label"]');

    de.forEach((query) => {
        let check = document.getElementById(query.htmlFor).checked;
        let name = query.querySelector('[id^="method-delete"]').textContent;
        mutations.push({'check': check, 'name': name});
    });

    let schemas = [];

    let s = document.querySelectorAll('[id^="label2-schema"]');

    s.forEach((schema) => {
        let check = document.getElementById(schema.htmlFor).checked;
        let name = schema.querySelector('[id^="label-schema"]').textContent;
        schemas.push({'check': check, 'name': name});
    });

    queries.filter((q) => {
        return !q.check
    }).forEach((q) => {
        openAPI.queries = openAPI.queries.filter((query) => {
            return query.name !== q.name;
        });
    });

    mutations.filter((q) => {
        return !q.check
    }).forEach((q) => {
        openAPI.mutations = openAPI.mutations.filter((query) => {
            return query.name !== q.name;
        });
    });

    schemas.filter((q) => {
        return !q.check
    }).forEach((q) => {
        openAPI.queries.forEach((query) => {
            if (query.response !== null) {
                if (query.response.schema.component.name === q.name) {
                    query.response = null;
                }
            }
        });

        openAPI.mutations.forEach((query) => {
            if (query.response !== null) {
                if (query.response.schema.component.name === q.name) {
                    query.response = null;
                }
            }
        });

        openAPI.mutations.forEach((query) => {
            if (query.request !== null) {
                if (query.request.schema.component.name === q.name) {
                    query.request = null;
                }
            }
        });
    });

    async function loadSourceCode() {

        var modal = document.getElementById("modal-loader");
        modal.style.display = "block";

        const response = await fetch('/source-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(openAPI)
        });


        if (response.ok) {
            document.getElementById("loader-icon").style.display = "none";
            document.getElementById("loader-text").style.display = "none";
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);

            let a = document.getElementById("downloak-link")
            a.style.display = "block";
            a.href = url;
            a.download = "source-code.zip";
            a.textContent = "Descargar código fuente";
            a.click(() => {window.location.href = '/';})
            window.location.href = "/";
        } else {
            alert("Something went wrong");
            window.location.href = "/";
        }


        // .then(blob => {
        //     // Crea un enlace para descargar el archivo ZIP
        //     const url = window.URL.createObjectURL(blob);
        //     const link = document.createElement('a');
        //     link.href = url;
        //     link.download = 'sourceCode.zip';
        //
        //     // Agrega el enlace al documento y haz clic en él para iniciar la descarga
        //     // document.body.appendChild(link);
        //     // link.click();
        //     //
        //     // // Limpia el enlace después de la descarga
        //     // link.remove();
        //     // window.URL.revokeObjectURL(url);
        // })
        // .catch(error => {
        //     // Se maneja cualquier error ocurrido durante la solicitud
        //     console.error(error);
        // });
    }

    loadSourceCode();
}


function main() {
    window.addEventListener('load', () => {
        loadTypeObject();
        updloadTypeObject();
    });
}

document.addEventListener('DOMContentLoaded', main);