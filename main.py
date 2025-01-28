from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Función para iniciar el bot
async def say_hello(update: Update, context: CallbackContext)-> None:
    # Botones inline del menú principal
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Presentación del bot ", callback_data="presentación"),
            InlineKeyboardButton(text="¿Qué es FMCPAY?", callback_data="FMCPAY_que"),
            InlineKeyboardButton(text="¿Para qué nos sirve FMCPAY?", callback_data="nos_sirve_para")
        ],
        [
            InlineKeyboardButton(text="¿Cómo registrarnos en FMCPAY?", callback_data="registrarnos")
        ],
        [
            InlineKeyboardButton(text="¿Cómo iniciar sesión y verificarnos en FMCPAY?", callback_data="como_iniciar_sesión"),
            InlineKeyboardButton(text="¿Cómo referir amigos en FMCPAY?", callback_data="como_referir")
        ],
        [
            InlineKeyboardButton(text="¿Cómo retirar en FMCPAY?", callback_data="retirar_FMCPAY")
        ],
        [
            InlineKeyboardButton(text="Enlaces", callback_data="enlaces")
        ],
         [
            InlineKeyboardButton(text="Videos", callback_data="Videos")
        ]
    ])
    
    # Respuesta inicial
    if update.message:  # Si es un mensaje directo
        await update.message.reply_text("Hola soy FMCPAYIJROY_bot, ¿en qué te puedo ayudar?", reply_markup=keyboard)
    elif update.callback_query:  # Si es un callback query
        await update.callback_query.answer()
        await update.callback_query.edit_message_text("Hola soy FMCPAYIJROY_BOT, ¿En qué te puedo ayudar?", reply_markup=keyboard)
    
    

# Función para manejar las respuestas a los botones
async def button_controller(update: Update, context: CallbackContext)-> None:
    query = update.callback_query
    await query.answer()  # Asegura que el callback se procese correctamente

     

    if query.data == "back_to_menu":
        await say_hello(update, context)  # Vuelve al menú principal
      

    # Respuestas a los botones principales
    if query.data == "registrarnos":
        # Submenú de ¿Cómo registrarnos en FMCPAY?
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="video", callback_data="Video_registro")],
            [InlineKeyboardButton(text="enlace", callback_data="Enlace_registro")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text( "Para registrarte en FMCPAY, lo primero que debes hacer es tocar mi enlace de invitación. Después, crea un nombre de usuario, una contraseña y agrega un email válido. Una vez completado este paso, haz clic en (Registrar). Rápidamente recibirás un código en tu correo para verificar tu email. Solo ingresa el código; con eso habrás finalizado tu registro y tendrás una cuenta activa en FMCPAY. Para mejor entendimiento, te dejo un video tutorial.",reply_markup=keyboard)
    
     # Respuestas a los botones principales de como iniciar sesión
    elif query.data == "como_iniciar_sesión":
        # Submenú de "¿Como iniciar sesión y verificarnos?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Video Tutorial ", callback_data="Video_inicio de sesión")],
            [InlineKeyboardButton(text="Enlace de Play Store", callback_data="Enlace_de_Play_Store")],
            [InlineKeyboardButton(text="Enlace de App Store", callback_data="Enlace_de_App_Store")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="atras_to_menu")]
        ])
        await query.edit_message_text("Para iniciar sesión en FMCPAY, lo primero que debes hacer es registrarte utilizando mi enlace de invitación o código. Si aún no lo has hecho, toca mi enlace y consulta mis opciones para que te enseñe cómo realizarlo correctamente. Una vez registrado, descarga la aplicación de FMCPAY desde la Play Store o App Store y abre la aplicación para iniciar sesión con tu cuenta. Al ingresar, verás una opción para verificar tu cuenta. Si no aparece automáticamente, toca la opción de verificación que aparece en pantalla para acceder a la verificación. Aquí se te mostrarán los requisitos necesarios para completar el proceso; haz clic en (Verificar) ahora y elige el método de verificación que prefieras (en mi caso, utilicé mi ID). A continuación, completa los datos solicitados en cada campo y presiona (Confirmar). Luego, se te pedirá tomar fotos del anverso y reverso de tu documento de identificación para validar los datos. Después de eso, haz clic en (Confirmar). También tendrás que tomarte una selfie para verificar que eres una persona real y que el documento que subiste es auténtico. Una vez completado todo, tu cuenta estará en proceso de aprobación, y en menos de 72 horas estará aprobada, permitiéndote comenzar a ganar sin límites. Para más ayuda y mejor aclaración, te dejo un video tutorial.", reply_markup=keyboard)

   # Respuestas a los botones principales
    elif query.data == "presentación":
        # Submenú de "¿Precentación del bot?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Video Tutorial", callback_data="Video_presentación")],
            [InlineKeyboardButton(text="Enlaces", callback_data="Enlace_presentación")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Hola, soy FMCPAYIJROY_bot y hoy te traigo la mejor forma de obtener ganancias ilimitadas desde la comodidad de tu casa, sin ningún tipo de inversión, de la manera más fácil y efectiva. Acá te dejo un video para que veas de lo que te hablo.", reply_markup=keyboard)

  # Respuestas a los botones principales
    elif query.data == "como_referir":
        # Submenú de "¿Como referir amigos en FMCPAY?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Video Tutorial", callback_data="Video_referir")],
            [InlineKeyboardButton(text="Enlaces", callback_data="Enlace_referir")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Para referir amigos en FMCPAY, lo primero que necesitas es tener una cuenta en la plataforma. Si aún no tienes una, puedes crearla fácilmente siguiendo mis opciones, donde te guiaré paso a paso en el proceso. Una vez que tengas tu cuenta, abre la aplicación en tu móvil o PC e inicia sesión con tu nombre de usuario y contraseña. Después, introduce el código de verificación que recibirás en tu correo electrónico para completar el acceso a tu cuenta. Ya dentro de la aplicación, haz clic en la opción indicada para obtener tu enlace de invitación. Copia el enlace proporcionado por la aplicación y, de esta forma, tendrás tu link de registro listo para compartirlo con tus amigos y comenzar a referir sin límites. Te dejo un video para mejor aclaración de dudas.", reply_markup=keyboard)

    # Respuestas a los botones principales
    elif query.data == "retirar_FMCPAY":
        # Submenú de "¿Cómo retirar en FMCPAY?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Video Tutorial de retiro", callback_data="Video_retirar")],
            [InlineKeyboardButton(text="¿Cómo verificar mi Google Authentication?", callback_data="verif_text")],
            [InlineKeyboardButton(text="¿Cómo comprar los PAYN ?", callback_data="Comprar_PAYN")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Para retirar en FMCPAY, primero debes iniciar sesión en la aplicación con tu nombre de usuario y contraseña. Una vez dentro, haz clic en la opción que aparece en la parte superior izquierda de la pantalla y luego en (Security) para verificar que tanto tu correo electrónico como tu Google Authentication estén configurados correctamente. Si no están verificados, consulta mis opciones para saber cómo hacerlo. Después de verificar ambos, el siguiente paso es vender los FMC que tengas por USDT. Para ello, regresa al menú principal y selecciona la opción (Trade). Luego, elige USDT y utiliza el buscador para encontrar FMC. Tócalo cuando aparezca y selecciona la opción de venta, que está etiquetada como (Sell). A continuación, revisa el precio de los FMC en ese momento y agrégalo a tu orden. Desliza la barra hasta el final y presiona (Sell FMC) para completar la venta. El siguiente paso es comprar PAYN, que es la moneda utilizada para cubrir la comisión de retiro. Consulta mis opciones para aprender cómo hacerlo.Una vez tengas los USDT y PAYN en tu billetera, toca la moneda USDT y completa los campos solicitados. Elige tu red preferida (por ejemplo, Tron TRC20), agrega la dirección de tu billetera y la cantidad que deseas retirar, y haz clic en (Withdraw) = (Retirar). Luego, se te pedirá confirmar la operación mediante un código enviado a tu correo y otro código para Google Authentication. Haz clic en (Send Code) para recibir el código en tu correo, ingrésalo rápidamente y confirma. Finalmente, haz clic en (OK) y ¡listo! El retiro se procesará y los fondos se depositarán al instante en tu billetera, sin demoras. Si todavía no sabes cómo hacerlo y tienes dudas, acá te dejo un Video Tutorial.", reply_markup=keyboard)

   
    # Respuestas a los botones principales
    elif query.data == "enlaces":
        # Submenú de "¿Enlaces?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Enlace de registro", callback_data="Enlace_1")],
            [InlineKeyboardButton(text="Enlace de inicio de sesión", callback_data="Enlace_2")],
            [InlineKeyboardButton(text="Enlace de la apk FMCPAY en Play Store", callback_data="Enlace_3")],
            [InlineKeyboardButton(text="Enlace de la apk  FMCPAY en App Store", callback_data="Enlace_4")],
            [InlineKeyboardButton(text="Enlace de la apk 2FAS Auth en Play Store ", callback_data="Enlace_5")],
            [InlineKeyboardButton(text="Enlace de la apk 2FAS Auth en APP Store ", callback_data="Enlace_6")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Acá te dejo los enlaces que te ayudarán ", reply_markup=keyboard)

# Respuestas a los botones principales
    elif query.data == "Videos":
        # Submenú de "¿Enlaces?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Video de presentación de FMCPAY", callback_data="Video_1")],
            [InlineKeyboardButton(text="Video de ¿Como registrame  en FMCPAY? ", callback_data="Video_2")],
            [InlineKeyboardButton(text="Video de inicio de sesión y verificación ", callback_data="Video_3")],
            [InlineKeyboardButton(text="Video de ¿Como referir amigos en FMCPAY", callback_data="Video_4")],
            [InlineKeyboardButton(text="Video de ¿Como retirar en FMCPAY?", callback_data="Video_5")],
            [InlineKeyboardButton(text="Video de verificar Google Authentication ", callback_data="Video_6")],
            [InlineKeyboardButton(text="Video de ¿Como comprar PAYN ? ", callback_data="Video_7")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Acá te dejo los videos tutoriales que te ayudarán a aclarar tus dudas paso a paso, en cada proceso. ", reply_markup=keyboard)

# Respuestas a los botones principales
    elif query.data == "FMCPAY_que":
        # Submenú de "¿Que es FMCPAY?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Enlaces", callback_data="enlace_FMCPAY")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("FMCPAY es una plataforma y aplicación Exchange innovadora que tiene como objetivo crear una puerta de entrada abierta y sin fisuras al espacio criptográfico. FMCPAY es una importante plataforma de intercambio de divisas digitales que permite a los usuarios comprar, vender e intercambiar una variedad de criptomonedas, incluidas Bitcoin, Ethereum y otras altcoins. También es reconocida por su gama de funciones dirigidas tanto a traders principiantes como experimentados.", reply_markup=keyboard)

# Respuestas a los botones principales
    elif query.data == "nos_sirve_para":
        # Submenú de "¿Para que nos sirve FMCPAY?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Cuanto gano al verificar cuenta", callback_data="bastante")],
            [InlineKeyboardButton(text="Cuanto gano al compartir con amigos", callback_data="mucho")],
            [InlineKeyboardButton(text="Enlaces", callback_data="enlace_Mio")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Pues en ella tenemos varias formas de generar ganancias, como, por ejemplo, por afiliados, verificando nuestra cuenta y por el intercambio de divisas.", reply_markup=keyboard)

# Respuestas a los subotones principales de como retirar
    elif query.data == "verif_text":
        # Submenú de "¿Cómo verificar mi Google Authentication?"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Enlaces de la aplicación 2FAS Auth(Play Store)", callback_data="enlace_2FAS_Play")],
            [InlineKeyboardButton(text="Enlaces de la aplicación 2FAS Auth(App Store)", callback_data="enlace_2FAS_App")],
            [InlineKeyboardButton(text="Video Tutorial", callback_data="Video_2FAS")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Para verificar tu Google Authentication, primero descarga la aplicación 2FAS Auth. Consulta mis opciones para obtener el enlace. Una vez descargada, abre la aplicación de FMCPAY e inicia sesión con tu usuario y contraseña. Dentro de la aplicación, haz clic en la opción (Security) y luego en (Google Authentication). Selecciona (Continuar) y copia el código de enlace proporcionado. Ingresa este código en la aplicación 2FAS Auth, que te generará un código. Ingresa este código en la aplicación de FMCPAY y confirma. ¡Listo! Tu Google Authentication estará verificado. Aquí te dejo un video tutorial. ", reply_markup=keyboard)

# Respuestas a los subotones principales de como retirar
    elif query.data == "Comprar_PAYN":
        # Submenú de "¿Cómo comprar los PAYN ? "
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Video tutorial ", callback_data="Video_PAYN")],
            [InlineKeyboardButton(text="Volver al menú principal", callback_data="back_to_menu")]
        ])
        await query.edit_message_text("Para comprar PAYN, abre la aplicación de FMCPAY e inicia sesión con tu usuario y contraseña. Dentro de la aplicación, haz clic en la opción (Trade), luego selecciona (USDT) y usa el buscador para encontrar PAYN. Tócalo cuando aparezca y selecciona la opción de compra (Buy). Verifica el precio de los PAYN en ese momento y agrégalo a tu orden. Desliza la barra hasta el final y presiona (Buy PAYN) para realizar la compra. Una vez realizada la compra, puedes vender los PAYN tocando la opción (Sell), verificando el precio de venta y agregándolo a nuestra orden. Seguidamente, arrastramos la opción mostrada hasta el final y le restamos 5 PAYN de la cantidad total. Ya para terminar, das clic en (Sell PAYN) y ¡listo! Para mejor ayuda, te dejo un video tutorial. Luego le damos clic en (Sell PAYN) y listo, ya tenemos nuestros 5 PAYN comprados. ", reply_markup=keyboard)

#  RESPUESTA Vuelve al menú principal
    elif query.data == "back_to_menu":
        await say_hello(update, context)  # Vuelve al menú principal

    

    # Submenú adicional de registro
    elif query.data == "Video_registro":
        await query.edit_message_text("Aquí tienes el video de ¿Cómo registrarme en FMCPAY?")
        await query.message.reply_video("BAACAgEAAxkBAAMQZ5hqoa83nLdsqEamJyszu8imCbAAAnkEAAJKUMhEK_6wXzut1U82BA")  # Reemplaza con el file_id real
  # File ID del video de registro

    elif query.data == "Enlace_registro":
        await query.edit_message_text("Aquí tienes el Enlace de Registro")
        await query.edit_message_text("https://fmcpay.com/auth/register?ref=667596638")   # Enlace de registro
    
    

    # Submenús adicional de inicio de sesión
    elif query.data == "Video_inicio de sesión":
        await query.edit_message_text("Aquí tienes el video de ¿Cómo iniciar sesión y verificarnos en FMCPAY?")
        await query.message.reply_video("BAACAgEAAxkBAAMTZ5hsMcMAAanwhZpcuOR4Zow9Vs5NAAJ7BAACSlDIRMtkQyswycl7NgQ") #  el file_id rea
    
     
    
    elif query.data == "Enlace_inicio de sesión":
        await query.edit_message_text("Aquí tienes el Enlace de inisio de sesión")
        await query.edit_message_text("https://fmcpay.com/auth/login")  # Enlace de inicio de sesión

    elif query.data == "Enlace_de_Play_Store":
        await query.edit_message_text("Aquí tienes el Enlace de FMCPAY en la Play Store")
        await query.edit_message_text("https://play.google.com/store/apps/details?id=com.bitcoinexc")   # Enlace de FMCPAY por la Play Store  

    elif query.data == "Enlace_de_App_Store":
        await query.edit_message_text("Aquí tienes el Enlace de FMCPAY en la App Store")  
        await query.edit_message_text("https://apps.apple.com/us/app/fmcpay/id1573381060?l=es-MX")   # Enlace de FMCPAY por App Store

   # Submenús adicional de referir
    elif query.data == "Video_referir":
        await query.edit_message_text("Aquí tienes el video de ¿Cómo referir amigos en FMCPAY?")
        await query.message.reply_video("BAACAgEAAxkBAAMSZ5hsMQ5zZclz3CTmydrpHDi-f4YAAnoEAAJKUMhEmTbaRqL1uHo2BA")  #el file_id real
    
    elif query.data == "Enlace_referir":
        await query.edit_message_text("Aquí tienes el Enlace de Cómo referir amigos en FMCPAY ")
        await query.edit_message_text("https://fmcpay.com/auth/login")   # Enlace de FMCPAY de inicio de sesión

     # Submenús adicional de retirar
    elif query.data == "Video_retirar":
        await query.edit_message_text("Aquí tienes el video de ¿Cómo retirar en FMCPAY?")
        await query.message.reply_video("BAACAgEAAxkBAAMMZ5hp7l0XLEdp_koNtv4C_xkmPM4AAncEAAJKUMhEaUciwKkjIjk2BA")    # File ID de Video de retiro
    
    
      
     # Submenús adicional de enlaces
    elif query.data == "Enlace_1":
        await query.edit_message_text("Aquí tienes el Enlace de registro de FMCPAY")
        await query.edit_message_text("https://fmcpay.com/auth/register?ref=667596638") # Enlace de registro

    elif query.data == "Enlace_2":
        await query.edit_message_text("Aquí tienes el Enlace de inico de sesión en FMCPAY")
        await query.edit_message_text("https://fmcpay.com/auth/login") # Enlace de inicio de sesión

    elif query.data == "Enlace_3":
        await query.edit_message_text("Aquí tienes el Enlace de la Play Store de FMCPAY")
        await query.edit_message_text("https://play.google.com/store/apps/details?id=com.bitcoinexc") # Enlace de la apk FMCPAY en Play Store
    
    elif query.data == "Enlace_4":
        await query.edit_message_text("Aquí tienes el Enlace de la App Store de FMCPAY")
        await query.edit_message_text("https://apps.apple.com/us/app/fmcpay/id1573381060?l=es-MX") # Enlace de la apk FMCPAY en App Store

    elif query.data == "Enlace_5":
        await query.edit_message_text("Aquí tienes el Enlace de la apk 2FAS Auth en Play Store")
        await query.edit_message_text("https://play.google.com/store/apps/details?id=com.twofasapp&pcampaignid=web_share") # Enlace de la apk 2FAS Auth en Play Store

    elif query.data == "Enlace_6":
        await query.edit_message_text("Aquí tienes el Enlace de la apk 2FAS Auth en App Store")
        await query.edit_message_text("https://apps.apple.com/us/app/2fa-authenticator-2fas/id1217793794?l=es-MX") # Enlace de la apk 2FAS Auth en App Store    

# Submenús adicional de Videos
    elif query.data == "Video_1":
        await query.edit_message_text("Aquí tienes el video de Presentación de FMCPAY")
        await query.message.reply_video("BAACAgEAAxkBAAMKZ5hoFOOzHzFIHi8f25uWIsUprAoAAnYEAAJKUMhEAVX_vVgtt7A2BA")   # Video de precentacion de FMCPAY

    elif query.data == "Video_2":
        await query.edit_message_text("Aquí tienes el video de ¿Como registrame  en FMCPAY?")
        await query.message.reply_video("BAACAgEAAxkBAAMQZ5hqoa83nLdsqEamJyszu8imCbAAAnkEAAJKUMhEK_6wXzut1U82BA")  # Video de ¿Como registrame  en FMCPAY?

    elif query.data == "Video_3":
        await query.edit_message_text("Aquí tienes el video de ¿Inicio de  sesión y verificacion?")
        await query.message.reply_video("BAACAgEAAxkBAAMTZ5hsMcMAAanwhZpcuOR4Zow9Vs5NAAJ7BAACSlDIRMtkQyswycl7NgQ")    # Video de inicio de sesión y verificacion

    elif query.data == "Video_4":
        await query.edit_message_text("Aquí tienes el video de ¿Como referir amigos en FMCPAY?")
        await query.message.reply_video("BAACAgEAAxkBAAMSZ5hsMQ5zZclz3CTmydrpHDi-f4YAAnoEAAJKUMhEmTbaRqL1uHo2BA")    #Video de ¿Como referir amigos en FMCPAY

    elif query.data == "Video_5":
        await query.edit_message_text("Aquí tienes el video de ¿Como retirar en FMCPAY?")
        await query.message.reply_video("BAACAgEAAxkBAAMMZ5hp7l0XLEdp_koNtv4C_xkmPM4AAncEAAJKUMhEaUciwKkjIjk2BA")    # Video de ¿Como retirar en FMCPAY?

    elif query.data == "Video_6":
        await query.edit_message_text("Aquí tienes el video de ¿Cómo verificar Google Authentication?")
        await query.message.reply_video("BAACAgEAAxkBAAMOZ5hqcTsqYGif6WyMW3SPXCLzdroAAngEAAJKUMhEUL0KcAnYHhs2BA")   # Video de verificar Google Authentication

    elif query.data == "Video_7":
        await query.edit_message_text("Aquí tienes el video de ¿Como comprar PAYN ?")
        await query.message.reply_video("BAACAgEAAxkBAAMIZ5hnODFZNEiGAsJ-iJLlaaejBKcAAnUEAAJKUMhEYAlENf3d21Q2BA")    #Video de ¿Como comprar PAYN ?

 # Submenús adicional de para que nos sirve?
    elif query.data == "bastante":
        await query.edit_message_text("Al verificar la cuenta en FMCPAY, nos da la aplicacion $2 dolares.")

    elif query.data == "mucho":
        await query.edit_message_text("Al compartir nuestro enlace de FMCPAY ganamos $2 dolares , pero solo si entran por nuestro enlace y verifican la cuenta.") 

    elif query.data == "enlace_Mio":
        await query.edit_message_text("Aquí tienes el Enlace de registro de FMCPAY")
        await query.edit_message_text("https://fmcpay.com/auth/register?ref=667596638")   # Enlace de registro

# Submenú de "¿Que es FMCPAY?"
    elif query.data == "enlace_FMCPAY":
        await query.edit_message_text("Aquí tienes el Enlace de FMCPAY")
        await query.edit_message_text("https://fmcpay.com/auth/register?ref=667596638")

# Submenú de "¿Precentación del bot?"
    elif query.data == "Video_presentación":
        await query.edit_message_text("Aquí tienes el video de Presentación de FMCPAY")
        await query.message.reply_video("BAACAgEAAxkBAAMKZ5hoFOOzHzFIHi8f25uWIsUprAoAAnYEAAJKUMhEAVX_vVgtt7A2BA")  # File ID de Video de precentacion

    elif query.data == "Enlace_presentación":
        await query.edit_message_text("Aquí tienes el Enlace de Presentación de FMCPAY")
        await query.edit_message_text("https://fmcpay.com/auth/register?ref=667596638")  # Enlace de registro

# Submenú de "¿Cómo verificar mi Google Authentication?"
    elif query.data == "enlace_2FAS_Play":
        await query.edit_message_text("Aquí tienes el Enlace de 2FAS Auth de la Play Store ")
        await query.edit_message_text("https://play.google.com/store/apps/details?id=com.twofasapp&pcampaignid=web_share") # Enlace  Google Authentication en Play Store

    elif query.data == "enlace_2FAS_App":
        await query.edit_message_text("Aquí tienes el Enlace de 2FAS Auth de la App Store")
        await query.edit_message_text("https://apps.apple.com/us/app/2fa-authenticator-2fas/id1217793794?l=es-MX") # Enlace  Google Authentication en App Store

    elif query.data == "Video_2FAS":
        await query.edit_message_text("Aquí tienes el video de ¿Cómo verificar mi Google Authentication?")
        await query.message.reply_video("BAACAgEAAxkBAAMOZ5hqcTsqYGif6WyMW3SPXCLzdroAAngEAAJKUMhEUL0KcAnYHhs2BA")  # File ID de Video de ¿Como verificar mi Google Authentication?

# Submenú de "¿Cómo comprar los PAYN ? "
    elif query.data == "Video_PAYN":
        await query.edit_message_text("Aquí tienes el video de ¿Cómo comprar los PAYN ?")
        await query.message.reply_video("BAACAgEAAxkBAAMIZ5hnODFZNEiGAsJ-iJLlaaejBKcAAnUEAAJKUMhEYAlENf3d21Q2BA")  # File ID de Video de ¿Como comprar PAYN?

async def go_back(update: Update, context: CallbackContext) -> None:
    # Regresar al menú inicial
    await say_hello(update, context)
 

# Inicializar la aplicación y el bot
application = ApplicationBuilder().token("7331119107:AAHnVWg_WSxpQKeC2BSICvHCOGdqbEAH6Gw").build()    # El token de mi bot FMCPAYIJROY_bot

# Los manejadores
application.add_handler(CommandHandler("start", say_hello))
application.add_handler(CallbackQueryHandler(button_controller))
application.add_handler(CallbackQueryHandler(go_back, pattern="back_to_menu"))  # Este handler maneja "back_to_menu"

# Correr el bot
application.run_polling(allowed_updates=Update.ALL_TYPES)












