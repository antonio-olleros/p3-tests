# Initalise project:

`poetry install`

# Content
### bas3-km1.xsd
- Taxonomy for Basel III Pillar 3 Key metrics (at consolidated group level)
- Reference https://www.bis.org/bcbs/publ/d455.pdf page 52

### km1-def.xml
- Definition linkbase - connects axes to domains and members
- Defines the valid members for each 'axis' (aka dimension)
- The file provided includes only the Regulatory Domain for illustrative purposes
- For production, it would need to be completed for the other axes including Framework, Tier and Output floor

### km1-pre.xml
- Presentation linkbase - table structure
- Defines how XBRL tools should present the taxonomy as a hierarchical table structure
- Again, this is illustrative and would need to be expanded to include the metric rows that need to be shown

### km1-labels.xml
- Labels
- Defines descriptive labels for concepts and members, again mainly for XBRL tools to provide a meaningful rendition of the table for collection or publication purposes
- e.g. ASF ('bas3-km1.xsd#bas3.ASF' in the taxonomy) is assigned the label 'Available Stable Funding'

## km1-cal.xml
- Calculations linkbase - optional summations
- Can optionally be used to define business logic, particularly validation sums (aka balance equalities) e.g. total capital should equal sum of capital breakdowns

