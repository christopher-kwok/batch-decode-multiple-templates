import os
import glob
from dbr import *

if __name__ == '__main__':
	try:
		# 1. Initialize license.
		# The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here is a free public trial license. Note that network connection is required for this license to work.
		# You can also request a 30-day trial license in the customer portal: https://www.dynamsoft.com/customer/license/trialLicense?architecture=dcv&product=dbr&utm_source=samples&package=python
		error = BarcodeReader.init_license('DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9')
		if error[0] != EnumErrorCode.DBR_OK:
			print("License error: "+ error[1])

		# 2. Create an instance of Barcode Reader.
		reader = BarcodeReader.get_instance()
		if reader == None:
			raise BarcodeReaderError('Get instance failed')

		# 3. Set image path.
		# Replace by your own image path.
		image_folder = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'images'

		# 4. Obtain current runtime settings of instance.
		default = reader.get_runtime_settings()

		# 5. Set expected barcode format.
		default.barcode_format_ids = EnumBarcodeFormat.BF_ONED | EnumBarcodeFormat.BF_QR_CODE | EnumBarcodeFormat.BF_DATAMATRIX

		# 6. Set expected barcode count.
		default.expected_barcodes_count = 1

		# 7. Retrieve image one by one from the folder.
		for idx, img in enumerate(glob.glob(os.path.join(image_folder, '*.*'))):

			# 8. Reset and apply default settings to the instance
			reader.reset_runtime_settings()
			reader.update_runtime_settings(default)

			print('Image', idx+1, img)
			# 9. Decode barcodes from an image file.
			text_results = reader.decode_file(img)

			# 10. Output the barcode text if barcode is found using default runtime settings
			if text_results != None:
				for text_result in text_results:
					print('Barcode Format:', text_result.barcode_format_string)
					print('Barcode Text:', text_result.barcode_text)
					print('Template: Default Runtime Settings')
			# 11. Output the barcode text if barcode is found using the JSON template
			else:
				# 12. Reset and apply JSON template to the instance
				reader.reset_runtime_settings()
				reader.init_runtime_settings_with_file(r'template-9.json')
				text_results = reader.decode_file(img)
				if text_results != None:
					for text_result in text_results:
						print('Barcode Format:', text_result.barcode_format_string)
						print('Barcode Text:', text_result.barcode_text)
						print('Template: JSON Template')
				# 13. If barcode cannot be found using any settings or templates.
				else:
					print('Barcode cannot be found using any settings or templates')

			print(40*'-')
		reader.recycle_instance()
	except BarcodeReaderError as bre:
		print(bre)