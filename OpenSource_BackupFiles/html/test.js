<style>
    #charlitosTable {
        width: 100%;
        border-collapse: collapse;
        font-family: Arial, sans-serif;
    }

    #charlitosTable th,
    #charlitosTable td {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }

    /* Archivo que vamos a respaldar */
    #charlitosTable .backup-row {
        background-color: #eaf2ff;
        font-weight: bold;
    }

    /* Línea que separa el archivo de sus conflictos */
    #charlitosTable .separator-row td {
        padding: 0;
        height: 5px;
        background-color: #aaa;
        border: none;
    }

    /* Espacio entre grupos de archivos */
    #charlitosTable .spacer-row td {
        height: 18px;
        padding: 0;
        border: none;
    }
</style>

<table id="charlitosTable">
    <thead>
        <tr>
            <th>File name</th>
            <th>Size</th>
            <th>Date modified</th>
            <th>Action</th>
        </tr>
    </thead>

    <tbody></tbody>
</table>

<script>
    function addRowToTable(
        fileName,
        sizeAsStr,
        dateModifiedAsStr,
        conflictedFiles
    ) {
        const tbody = document.querySelector("#charlitosTable tbody");

        // Crea un renglón con cuatro columnas.
        function createRow(name, size, date, action) {
            const row = document.createElement("tr");

            for (const value of [name, size, date, action]) {
                const cell = document.createElement("td");
                cell.textContent = value;
                row.appendChild(cell);
            }

            return row;
        }

        // 1. Archivo que vamos a respaldar.
        const backupRow = createRow(
            fileName,
            sizeAsStr,
            dateModifiedAsStr,
            ""
        );

        backupRow.classList.add("backup-row");
        tbody.appendChild(backupRow);

        // Si recibimos null, lo tratamos como una lista vacía.
        const conflicts = conflictedFiles ?? [];

        if (conflicts.length > 0) {
            // 2. Separador que ocupa las cuatro columnas.
            const separatorRow = document.createElement("tr");
            separatorRow.classList.add("separator-row");

            const separatorCell = document.createElement("td");
            separatorCell.colSpan = 4;

            separatorRow.appendChild(separatorCell);
            tbody.appendChild(separatorRow);

            // 3. Un renglón por cada archivo con conflicto.
            for (const conflict of conflicts) {
                const conflictName = conflict[0];
                const conflictPath = conflict[1];
                const conflictSize = conflict[2];
                const conflictDate = conflict[3];

                const conflictRow = createRow(
                    conflictPath,
                    conflictSize,
                    conflictDate,
                    ""
                );

                // Muestra el nombre al dejar el cursor sobre la ruta.
                conflictRow.cells[0].title = conflictName;

                tbody.appendChild(conflictRow);
            }
        }

        // 4. Espacio antes del siguiente grupo.
        const spacerRow = document.createElement("tr");
        spacerRow.classList.add("spacer-row");

        const spacerCell = document.createElement("td");
        spacerCell.colSpan = 4;

        spacerRow.appendChild(spacerCell);
        tbody.appendChild(spacerRow);
    }
</script>