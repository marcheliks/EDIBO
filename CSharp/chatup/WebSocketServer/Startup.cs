using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Net.WebSockets;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;

namespace WebSocketServer
{
    public class Startup
    {
        
        public void ConfigureServices(IServiceCollection services)
        {
        }

        
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
          {
            app.UseWebSockets();

            app.Use(async (context, next) =>
          {
            //Add the call to print the Request parameters here
            WriteRequestParam(context, env);

            if (context.WebSockets.IsWebSocketRequest)
          {
            WebSocket webSocket = await context.WebSockets.AcceptWebSocketAsync();
            Console.WriteLine("WebSocket Connected");

            await ReceiveMessage(webSocket, async (result, buffer) =>
            {
              if (result.MessageType == WebSocketMessageType.Text)
              {
                Console.WriteLine($"Receive->Text");

                return;
              }
              else if (result.MessageType == WebSocketMessageType.Close)
              {
                Console.WriteLine($"Receive->Close");

                return;
              }
            });
          }
          else
          {
              Console.WriteLine("Hello from 2nd Request Delegate - No WebSocket");
              await next();
          }
        });
          }
        public void WriteRequestParam(HttpContext context, IHostingEnvironment env)
          {
            if (env.IsDevelopment())
            {
              Console.WriteLine(Environment.NewLine + "Request Method: " + context.Request.Method);
              Console.WriteLine("Request Protocol: " + context.Request.Protocol);

              if (context.Request.Headers != null)
              {
                Console.WriteLine("Request Headers: ");
                foreach (var h in context.Request.Headers)
                {
                  Console.WriteLine("--> " + h.Key + ": " + h.Value);
                }
              }
            }
          }
          private async Task ReceiveMessage(WebSocket socket, Action<WebSocketReceiveResult, byte[]> handleMessage)
            {
              var buffer = new byte[1024 * 4];
              while (socket.State == WebSocketState.Open)
              {
                var result = await socket.ReceiveAsync(buffer: new ArraySegment<byte>(buffer),
                   cancellationToken: CancellationToken.None);
               handleMessage(result, buffer);
              }
            } 
     }
     
  }
        