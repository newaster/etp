


document.getElementById('select-picture-button').addEventListener('click', function() {
    document.getElementById('profile-picture').click();
  });

  document.getElementById('profile-picture').addEventListener('change', function() {
    document.getElementById('submit-button').click();
  });



    function showEditAlert(itemId,csrf) {
        // Get the description and status elements for the current item
        var descriptionElement = document.getElementById('description-' + itemId);
        var statusElement = document.getElementById('status-' + itemId);

        // Prompt the user to enter a new description
        var newDescription = prompt('Enter a new description:');
        if (newDescription !== null) {
            // If the user clicked "OK" and entered a description, update the elements
            descriptionElement.textContent = newDescription;
            statusElement.textContent = 'Done';

            // Send the updated data to the server
            var url = '/editticket/' + itemId ;
            var data = {
                description: newDescription,
                status: 'Done'
            };
            var csrftoken = csrf

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                alert('Status updated successfully.');
            })
            .catch(error => {
                alert('Error occurred while updating the description. Please try again.');
            });
        } else {
            // If the user clicked "Cancel" or didn't enter a description, show a message
            alert('Description update canceled.');
        }
    }



    function showaddcredit(itemId,csrf) {
        // Get the description and status elements for the current item
        var descriptionElement = document.getElementById('quota-' + itemId);
        //console.log(descriptionElement)

        // Prompt the user to enter a new description
        var newDescription = prompt('Enter no of Credits:');
        //console.log(newDescription)
        if (newDescription !== null) {
            // If the user clicked "OK" and entered a description, update the elements
            descriptionElement.textContent = newDescription;

            // Send the updated data to the server
            var url = '/addcredit/' + itemId ;
            var data = {
                quota: newDescription,
            };
            var csrftoken = csrf

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                alert('Credit Added successfully.');
            })
            .catch(error => {
                alert('Error occurred while adding Credit. Please try again.');
            });
        } else {
            // If the user clicked "Cancel" or didn't enter a description, show a message
            alert('Canceled.');
        }
    }









    function generatePDF() {
      const table = document.getElementById('myTable');

      // Convert the table to a canvas using html2canvas
      html2canvas(table).then((canvas) => {
        const imgData = canvas.toDataURL('image/png');
        const pdf = new jspdf.jsPDF();
        
        // Customize the PDF layout as needed
        const pdfWidth = pdf.internal.pageSize.getWidth();
        const pdfHeight = pdf.internal.pageSize.getHeight();
        const contentWidth = pdfWidth - 10; // Adjust the content width as needed
        
        // Header Photo
        const headerPhotoWidth = 50;
        const headerPhotoHeight = 25;
        const headerPhotoX = 5;
        const headerPhotoY = 5;
        const headerPhotoPath = "{% static 'images/header.png' %}";
        pdf.addImage(headerPhotoPath, "PNG", headerPhotoX, headerPhotoY, headerPhotoWidth, headerPhotoHeight);
        
        // Footer Photo
        const footerPhotoWidth = 150;
        const footerPhotoHeight = 25;
        const footerPhotoX = pdfWidth - footerPhotoWidth - 40;
        const footerPhotoY = pdfHeight - footerPhotoHeight ;
        const footerPhotoPath = "{% static 'images/footer.png' %}";
        pdf.addImage(footerPhotoPath, "PNG", footerPhotoX, footerPhotoY, footerPhotoWidth, footerPhotoHeight);
        
        // Header Text
        pdf.setFontSize(14);
        const title = document.title;
        pdf.text(title, headerPhotoX + headerPhotoWidth + 40, headerPhotoY + headerPhotoHeight / 2);
        
       
        
        // Content (Table)
        const imageWidth = contentWidth;
        const imageHeight = (imageWidth / canvas.width) * canvas.height;
        const contentHeight = pdfHeight - 30 - imageHeight - 20; // Adjust the spacing and heights as needed
        
        pdf.addImage(imgData, 'PNG', (pdfWidth - imageWidth) / 2, 40, imageWidth, imageHeight); // Position and size the image

        // Download the PDF file
        pdf.save(title+'.pdf');
      });
    }

    // Trigger the PDF generation when a button is clicked
    document.getElementById('generateButton').addEventListener('click', generatePDF);





 