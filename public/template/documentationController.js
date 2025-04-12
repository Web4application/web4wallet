const mustache = require('mustache');
const fs = require('fs');
const path = require('path');

// Sample data to pass to the template
const data = {
  container: {
    isClassOrEnum: true,
    hasPublicConstructors: true,
    publicConstructorsSorted: [
      { shortName: "Constructor1", href: "#constructor1", isDeprecated: false },
      { shortName: "Constructor2", href: "#constructor2", isDeprecated: true }
    ]
  }
};

// Path to the Mustache template file
const templatePath = path.join(__dirname, '../views/documentation.mustache');

// Read the template file
fs.readFile(templatePath, 'utf8', (err, template) => {
  if (err) {
    console.error('Error reading template:', err);
    return;
  }

  // Render the template with the data
  const rendered = mustache.render(template, data);

  // Here, you can send the rendered HTML as a response
  console.log(rendered);  // For now, we'll just log it to the console
});
