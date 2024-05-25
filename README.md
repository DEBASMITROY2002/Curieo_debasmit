# Error Log Monitor System

## Overview

This repository contains the solution for the Curieo.org assignment, specifically an Error Log Monitor System implemented in Python 3.9.

## Prerequisites

- Python 3.9

## Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/DEBASMITROY2002/Curieo_debasmit.git
   ```

2. Navigate to the repository folder:
   ```sh
   cd Curieo_debasmit
   ```
3. Create an 'input.txt' file in the repository folder to provide input data.

Sample input.txt Format
```
1715744138011;INTERNAL_SERVER_ERROR;23.72
1715744138012;INTERNAL_SERVER_ERROR;10.17
INTERNAL_SERVER_ERROR
1715744138012;BAD_REQUEST;15.22
1715744138013;INTERNAL_SERVER_ERROR;23.72
BEFORE 1715744138011
AFTER 1715744138010
BEFORE INTERNAL_SERVER_ERROR 1715744138011
AFTER INTERNAL_SERVER_ERROR 1715744138010
```

Note: Error types should not contain any non-alphanumeric characters except underscores. Ensure there are no extra whitespaces.

